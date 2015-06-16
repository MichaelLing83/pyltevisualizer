#!/usr/bin/env python3


import nose
import argparse

# parse command line arguments
class Args:
    '''
    Class used to save command line argument parsing results, and some global parameters.
    '''
    pass

parser = argparse.ArgumentParser(description='Run nosetests from current directory.')
parser.parse_args(namespace=Args)

nose.main()
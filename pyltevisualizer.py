#!/usr/bin/env python3

import argparse
from ts36_211.core.Frame import Frame
from ts36_211.L1Config import L1Config
from ts36_211.core.Plotter import Plotter
import logging

# parse command line arguments
class Args:
    '''
    Class used to save command line argument parsing results, and some global parameters.
    '''
    pass

parser = argparse.ArgumentParser(description='ltepyvisualizer helps to visualize LTE-A RE allocation.')
parser.add_argument('-o', '--output-file', type=str, default='ltepyvisualizer_output.png', help='Save output as this given name.')
parser.add_argument("-v", "--verbosity", help="verbosity of logging output [0..4]", action="count", default=0)
parser.parse_args(namespace=Args)

if Args.verbosity > 4:
    Args.verbosity = 4
log_lvl = (logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG)[Args.verbosity]
logging.basicConfig(level=log_lvl, format='%(filename)s:%(levelname)s:%(message)s')
frame = Frame(L1Config())
plotter = Plotter(frame)
plotter.plot(Args.output_file)
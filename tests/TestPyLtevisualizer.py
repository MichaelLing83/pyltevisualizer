import unittest
import subprocess
import os
from nose.tools import eq_, assert_is_not_none

class TestPyltevisualizer(unittest.TestCase):
    exe_file = None
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == 'pyltevisualizer.py':
                 exe_file = os.path.join(root, file)
    assert_is_not_none(exe_file)
    def test_default_run(self):
        eq_(0, subprocess.call('python3 {}'.format(TestPyltevisualizer.exe_file), shell=True))
# pyltevisualizer
[![Build Status](https://travis-ci.org/MichaelLing83/pyltevisualizer.svg?branch=master)](https://travis-ci.org/MichaelLing83/pyltevisualizer)

This used to be code.google.com/p/pyltevisualizer, and now it continues on GitHub. After years, there are so many changes in the world of LTE (or LTE-A, -B, ...). It is time to restart this project!


## Requirements
* Output a picture to show Uu interface RE usage, in which:
 * it is able to distinguish different antenna ports (by color);
 * it is able to distinguish different physical channels (by color);
 * colors are configurable;
* Support [3GPP 36.211 Release 12] (http://www.etsi.org/deliver/etsi_ts/136200_136299/136211/12.04.00_60/ts_136211v120400p.pdf);
* Support FDD and TDD;
* OK performance;
* Run on Linux, Windows, MacOS
* Easy to download and run

## Design Decisions
* Implement in Python 3;
* Test framework is nose;
* Package/Module split ([Issue 6] (https://github.com/MichaelLing83/pyltevisualizer/issues/6)):
 * Follow [this document] (https://docs.python.org/3/tutorial/modules.html) to construct folder/file structures;
 * Split according to 36 serial specification chapters and sections;
 * E.g.: ts36_211.ch7.s5 for TS36.211, Chapter 7, Section 5;
* Naming rules:
 * Variables ([Issue 11] (https://github.com/MichaelLing83/pyltevisualizer/issues/11)):
   * Follow the name in spec as much as possible;
    * If the symbol in spec has upper/lower-fix, then put upper-fix first, and split them with a '_';
    * Ignore characters not in [a-zA-Z_];
    * E.g.: N_cell_ID, N__CPl, n_3p_PUCCH, s_p_l;

## HowTo
* Setup environment
 1. go to root folder that contains `setenv.sh`
 2. `source setenv.sh`
* Run test
 1. go to any folder
 2. execute `test` to run all tests recursively from current folder

## Known Limitations
* MBSFN is not supported;
* 7.5 kHz subcarrier is not supported;

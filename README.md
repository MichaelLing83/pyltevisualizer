# pyltevisualizer
Automatically exported from code.google.com/p/pyltevisualizer

Now continues on GitHub. After years, there are so many changes in the world of LTE (or LTE-A, -B, ...). It is time to restart this project!


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
* Package/Module split [Issue 6] (https://github.com/MichaelLing83/pyltevisualizer/issues/6):
  * Follow [this document] (https://docs.python.org/3/tutorial/modules.html) to construct folder/file structures;
  * Split according to 36 serial specification chapters and sections;

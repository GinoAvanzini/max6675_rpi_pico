#!/usr/bin/env python

import sys, os
from serial.tools.list_ports import grep

def main(grep_string):
    serialifaces = grep(grep_string)
    try:
        iface = next(serialifaces)
        print(iface.device)
        sys.exit(0)
    except StopIteration:
        sys.exit(-1)
    except Exception:
        sys.exit(-2)

if __name__ == "__main__":

    if(len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        sys.exit(-2)


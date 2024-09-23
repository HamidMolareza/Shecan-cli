#!/usr/bin/env python3

import sys

from libs.ColorPrint import ColorPrint
from libs.Shecan import Shecan


# TODO: Use command line library


def print_help():
    ColorPrint.info("commands: enable, disable, status")


def main():
    if len(sys.argv) != 2:
        ColorPrint.error("Input is not valid.")
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()
    shecan = Shecan()
    if command == "disable":
        shecan.disable()
    elif command == "enable":
        shecan.enable()
    elif command == "status":
        shecan.status()
    else:
        ColorPrint.error("Command is not valid.")
        print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()

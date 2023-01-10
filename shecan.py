import os.path
import re
import sys

# TODO: After update file, reload service


def disable(file_path: str):
    data = read_all_text(file_path)
    data = re.sub("nameserver [0-9.]*", "", data).strip()
    write_all_text(file_path, data)


def enable(file_path: str):
    disable(file_path)
    data = read_all_text(file_path)
    data += "\nnameserver 185.51.200.2\nnameserver 178.22.122.100\n"
    write_all_text(file_path, data)


def read_all_text(file_path: str) -> str:
    if not os.path.isfile(file_path):
        return ""
    file = open(file_path, "r")
    return file.read()


def write_all_text(file_path: str, data: str):
    file = open(file_path, "w")
    file.write(data)


def main():
    if len(sys.argv) >= 3:
        print("Only one parameter is accepted. 'enable' or 'disable'")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Input is not valid. Specify whether you want to 'enable' or 'disable' the Shecan?!")
        sys.exit(1)

    command = sys.argv[1].lower()
    file_path = "/etc/resolvconf/resolv.conf.d/base-test"  # TODO: Remove test from file name
    if command == "disable":
        disable(file_path)
    elif command == "enable":
        enable(file_path)
    else:
        print("Command is not valid. Use enable or disable command.")
        sys.exit(1)


if __name__ == '__main__':
    main()

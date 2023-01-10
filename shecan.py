import os
import sys
import re


def disable():
    connection_name = get_active_connection_name()
    os.system(f"nmcli connection modify \"{connection_name}\" ipv4.dns \"\"")
    os.system(f"nmcli connection modify \"{connection_name}\" ipv4.ignore-auto-dns no")
    os.system(f"nmcli connection modify \"{connection_name}\" ipv6.method auto")
    restart_connection(connection_name)


def enable():
    connection_name = get_active_connection_name()
    os.system(f"nmcli connection modify \"{connection_name}\" ipv4.dns \"185.51.200.2, 178.22.122.100\"")
    os.system(f"nmcli connection modify \"{connection_name}\" ipv4.ignore-auto-dns yes")
    os.system(f"nmcli connection modify \"{connection_name}\" ipv6.method disabled")
    restart_connection(connection_name)


def get_active_connection_name() -> str:
    data = os.popen("nmcli con show --active | grep wifi").read()
    return re.split("[ \t]{2,}", data)[0]  # Split base 2 or more white space


def restart_connection(connection_name: str):
    os.system(f"nmcli con down \"{connection_name}\"")
    os.system(f"nmcli con up \"{connection_name}\"")


def main():
    if len(sys.argv) >= 3:
        print("Only one parameter is accepted. 'enable' or 'disable'")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Input is not valid. Specify whether you want to 'enable' or 'disable' the Shecan?!")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "disable":
        disable()
    elif command == "enable":
        enable()
    else:
        print("Command is not valid. Use 'enable' or 'disable' command.")
        sys.exit(1)


if __name__ == '__main__':
    main()

import os
import re


class Nmcli:
    @staticmethod
    def modify_connection(connection_name: str, key: str, value: str):
        os.system(f"nmcli connection modify \"{connection_name}\" \"{key}\" \"{value}\"")

    @staticmethod
    def get_connection_info(connection_name: str, key: str) -> str:
        return os.popen(f"nmcli connection show {connection_name} | grep \"{key}\"").read().split()[1]

    @staticmethod
    def connect(connection_name: str):
        os.system(f"nmcli con up \"{connection_name}\"")

    @staticmethod
    def disconnect(connection_name: str):
        os.system(f"nmcli con down \"{connection_name}\"")

    @staticmethod
    def restart_connection(connection_name: str):
        Nmcli.disconnect(connection_name)
        Nmcli.connect(connection_name)

    @staticmethod
    def get_active_connection_name() -> str:
        data = os.popen("nmcli con show --active | grep wifi").read()
        return re.split("[ \t]{2,}", data)[0]  # Split base 2 or more white space

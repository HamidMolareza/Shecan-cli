from libs.ColorPrint import ColorPrint
from libs.Nmcli import Nmcli


class Shecan:
    _shecan_dns_list = ["185.51.200.2", "178.22.122.100"]

    @staticmethod
    def disable():
        connection_name = Nmcli.get_active_connection_name()
        Nmcli.modify_connection(connection_name, "ipv4.dns", "")
        Nmcli.modify_connection(connection_name, "ipv4.ignore-auto-dns", "no")
        Nmcli.modify_connection(connection_name, "ipv6.method", "auto")
        Nmcli.restart_connection(connection_name)

    def enable(self):
        connection_name = Nmcli.get_active_connection_name()
        shecan_dns = ", ".join(self._shecan_dns_list)
        Nmcli.modify_connection(connection_name, "ipv4.dns", shecan_dns)
        Nmcli.modify_connection(connection_name, "ipv4.ignore-auto-dns", "yes")
        Nmcli.modify_connection(connection_name, "ipv6.method", "disabled")
        Nmcli.restart_connection(connection_name)

    def status(self):
        connection_name = Nmcli.get_active_connection_name()
        dns = Nmcli.get_connection_info(connection_name, "ipv4.dns:")
        if set(dns.split(",")) == set(self._shecan_dns_list):
            ColorPrint.success(f"Ipv4 dns is set and valid. {dns}")
        elif dns == "--":
            ColorPrint.error(f"Ipv4 dns is not set. {dns}")
        else:
            ColorPrint.error(f"Ipv4 dns is set but is not shecan dns. {dns}")

        ignore_auto_dns = Nmcli.get_connection_info(connection_name, "ipv4.ignore-auto-dns")
        if ignore_auto_dns.lower() == "yes":
            ColorPrint.success("Ipv4 auto dns is disable and Ok.")
        else:
            ColorPrint.warning("Ipv4 auto dns is not disable. It is better to turn it of.")

        ipv6 = Nmcli.get_connection_info(connection_name, "ipv6.method")
        if ipv6.lower() == "disabled":
            ColorPrint.success("Ipv6 is disable and Ok.")
        else:
            ColorPrint.warning("Ipv6 is not disable. It is better to turn it of.")

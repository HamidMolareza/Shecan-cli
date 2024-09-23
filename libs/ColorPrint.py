from colorama import Fore, Style


class ColorPrint:
    @staticmethod
    def error(text: str):
        print(Fore.RED + text + Style.RESET_ALL)

    @staticmethod
    def success(text: str):
        print(Fore.GREEN + text + Style.RESET_ALL)

    @staticmethod
    def warning(text: str):
        print(Fore.YELLOW + text + Style.RESET_ALL)

    @staticmethod
    def info(text: str):
        print(text)

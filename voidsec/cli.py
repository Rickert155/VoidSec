from voidsec.colors import RESET, RED, GREEN, BOLD
from voidsec.core import greeting
from voidsec.package import get_packages_list 

def main():
    greeting()
    packages_list = get_packages_list()
    if len(packages_list) > 0:
        print(f"{GREEN}Список доступных модулей:{RESET}")
        for index, package in enumerate(packages_list, start=1):
            print(
                    f"{RED}[{index}]{RESET} {BOLD}{package['name']}"
                    f" - {package['description']}{RESET}\n"
                    f"\tURL: {package['source']}"
                    )

import json
import os
import sys
import subprocess
from __init__ import __author__, __version__, __project__
from voidsec.colors import RED, GREEN, RESET, BOLD, YELLOW
from voidsec.config import packages_dir, package_json

def greeting() -> None:
    text = (
            f"Project:\t{BOLD}{__project__}{RESET}\n"
            f"Version:\t{BOLD}{__version__}{RESET}\n"
            f"Author:\t\t{BOLD}{__author__}{RESET}\n"
            )
    print(text)

def get_packages_list() -> list[dict]:
    """get meta info"""
    packages_dir_list = sorted([
        f"{packages_dir}/{package_dir}" for package_dir in os.listdir(packages_dir)
        ])
    packages_list = []
    for package_dir in packages_dir_list:
        package = f"{package_dir}/{package_json}"
        with open(package, "r") as file:
            data = json.load(file)
        meta_info = {
                "name":data.get("name"),
                "description":data.get("description"),
                "source":data.get("source"),
                "path":package
                }
        packages_list.append(meta_info)
    return packages_list

def show_packages_list():
    packages_list = get_packages_list()
    for count, package in enumerate(packages_list, start=1):
        print(
                f"{RED}[{count}]{RESET} {BOLD}{GREEN}{package['name']}{RESET} "
                f"{BOLD}{package['description']}{RESET}\n"
                f"\t{YELLOW}URL: {package['source']}{RESET}"
                )


def check_package(package_name:str):
    packages_paths = [package["path"] for package in get_packages_list()]
    package = f"{packages_dir}/{package_name}/{package_json}"
    if package not in packages_paths:
        sys.exit(f"{RED}Package {BOLD}{package_name}{RESET} {RED}not found!{RESET}")
    return package

def run_command(command:str) -> None:
    print(f"{GREEN}command: {command}{RESET}")
    subprocess.run(command, shell=True)

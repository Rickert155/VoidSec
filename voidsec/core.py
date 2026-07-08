import subprocess
from __init__ import __author__, __version__, __project__
from voidsec.colors import RED, GREEN, RESET, BOLD

def greeting():
    text = (
            f"Project:\t{BOLD}{__project__}{RESET}\n"
            f"Version:\t{BOLD}{__version__}{RESET}\n"
            f"Author:\t\t{BOLD}{__author__}{RESET}\n"
            )
    print(text)

def run_command(command:str):
    print(f"command: {command}")
    subprocess.run(command, shell=True)

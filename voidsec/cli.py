import sys
from voidsec.colors import RESET, RED, GREEN, BOLD
from voidsec.core import (
        greeting, 
        show_packages_list,
        )
from voidsec.build import package_build
from voidsec.delete import package_delete

MODES = {
        "--build":{
            "helper":"python3 -m voidsec --build <tool>",
            "command":package_build,
            "add_args":True
            },
        "--update":{
            "helper":"python3 -m voidsec --update <tool>",
            "command":package_build,
            "add_args":True
            },
        "--delete":{
            "helper":"python3 -m voidsec --delete <tool>",
            "command":package_delete,
            "add_args":True
            },
        "--list":{
            "helper":"python3 -m voidsec --list",
            "command":show_packages_list,
            "add_args":False
            },
        "--help":{
            "helper":"python3 -m voidsec --build --help"
            }
        }


def main():

    greeting()
    modes_avail = [mode for mode in MODES] #modes list
    params = sys.argv[1:]
    if len(params) == 0:
        sys.exit(show_packages_list())
    mode = params[0]
    if mode not in modes_avail:
        sys.exit(
                f"{RED}Mode '{mode}' not defined!{RESET}\n"
                f"{RED}Modes avail: {modes_avail}{RESET}"
                )
    helper = MODES[mode].get("helper")
    if "--help" in params:
        sys.exit(
                f"Mode:\t\t{GREEN}{mode}\n{RESET}"
                f"Template:\t{BOLD}{helper}{RESET}"
                )
    elif MODES[mode].get("add_args"):
        if len(params) > 1:
            MODES[mode].get("command")(package_name=params[1])
        else:
            sys.exit(f"Template: {RED}{BOLD}{helper}{RESET}")
    elif MODES[mode].get("add_args") == False:
        MODES[mode].get("command")()

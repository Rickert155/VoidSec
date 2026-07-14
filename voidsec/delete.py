import json
import sys
from voidsec.config import packages_dir, package_json
from voidsec.core import get_packages_list, run_command, check_package

def package_delete(package_name:str) -> None:
    package = check_package(package_name=package_name)
    with open(package, "r") as file:
        data = json.load(file)
    image_name = data["image"]
    command = f"podman image rm {image_name}"
    run_command(command=command)


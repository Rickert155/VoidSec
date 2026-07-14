import json
import sys
from voidsec.config import packages_dir, package_json
from voidsec.core import get_packages_list, run_command, check_package


def package_build(package_name:str) -> None:
    package = check_package(package_name=package_name)

    with open(package, "r") as file:
        data = json.load(file)
    containerfile = data["containerfile"]
    image_name = data["image"]

    path_containerfile = package.replace(package_json, containerfile)

    command = f"podman build -t {image_name} -f {path_containerfile}"
    run_command(command=command)

import json
import sys
import os
from voidsec.config import packages_json, package_json
from voidsec.colors import RED, GREEN, RESET, BOLD

def fields_packages_json() -> dict:
    try:
        fields = {}
        with open(packages_json, "r") as file:
            data = json.load(file)

        for key, value in data.items():
            fields[key] = value
        
        return fields
    except FileNotFoundError:
        sys.exit(f"{RED}{BOLD}{packages_json} not found!{RESET}")

def get_packages_list() -> list[str]:
    packages_dir = fields_packages_json()["package_dir"]
    packages_dir_list = []
    for package_dir in os.listdir(packages_dir):
        packages_dir_list.append(f"{packages_dir}/{package_dir}")

    packages_dir_list = sorted(packages_dir_list)
    
    packages_list = []
    for package_dir in packages_dir_list:
        package_config = f"{package_dir}/{package_json}"
        if os.path.exists(package_config):
            with open(package_config, "r") as file:
                data = json.load(file)
            name = data.get("name")
            description = data.get("description")
            source = data.get("source")
            packages_list.append({
                "name":name, 
                "description":description,
                "source":source
                })

    return packages_list




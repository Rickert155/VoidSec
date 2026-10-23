from voidsec.core import get_packages_list 
from voidsec.colors import GREEN, RED, RESET, BOLD, BLUE, YELLOW

def search(package_name:str|list[str]) -> None:
    key = package_name # Вынужденная мера, вытекает из реализации парсера
    key = key.lower()
    
    result_search = []
    
    for package in get_packages_list():
        name = package["name"]
        description = package["description"]
        category = package["category"]

        meta_package = f"{name} {description} {category}"
        meta_package = (
                meta_package.\
                        replace(" | ", " ").\
                        replace(",", " ").\
                        replace("/", " ").\
                        replace("  ", "")
                )
        meta_package = meta_package.split(" ")
        for word in meta_package:
            word = word.lower()
            if key in word:
                if package not in result_search:
                    result_search.append(package)

    for count_package, package in enumerate(result_search, start=1):
        name = package["name"]
        description = package["description"]
        category = package["category"]
        source = package["source"]

        text = (
                f"{RED}[{count_package}]{RESET} "
                f"{GREEN}{BOLD}{name}{RESET} [{category}]\n"
                f"{BLUE}{description}{RESET}\n"
                f"{YELLOW}URL: {source}{RESET}\n"
                )
        print(text)
    
    if len(result_search) == 0:
        print(f"{RED}Keyword {BOLD}{key}{RESET}{RED} not found!{RESET}")

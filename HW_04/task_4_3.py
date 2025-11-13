import sys
from pathlib import Path
from colorama import init, Fore, Style

init()

def display_directory_structure(path, indent=0):
    """
    Recursively displays the directory structure.
    
    Args:
        path: Path object of the directory
        indent: indentation level (for nesting)
    """
    try:
        for item in path.iterdir():
            spacing = "  " * indent
            
            if item.is_dir():
                print(f"{spacing}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                display_directory_structure(item, indent + 1)
            else:
                print(f"{spacing}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        spacing = "  " * indent
        print(f"{spacing}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_4_3.py <directory_path>")
        return
    
    directory_path = sys.argv[1]
    path = Path(directory_path)
    
    if not path.exists():
        print(f"{Fore.RED}Error: Path '{directory_path}' does not exist{Style.RESET_ALL}")
        return
    
    if not path.is_dir():
        print(f"{Fore.RED}Error: '{directory_path}' is not a directory{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}Directory structure: {path}{Style.RESET_ALL}\n")
    display_directory_structure(path)

if __name__ == "__main__":
    main()
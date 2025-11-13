from pathlib import Path

def get_cats_info(path):
    cats = []
    path = Path(path)  # Convert string path argument to Path object
    
    if not path.exists():  # Check if file exists
        print(f"Error: The file at {path} does not exist.")
        return cats         # Return empty list if file does not exist
    
    if not path.is_file():  # Check if it's a file
        print(f"Error: The path {path} is not a file.")
        return cats         # Return empty list if not a file
    
    with path.open('r', encoding='utf-8') as file:
        for line in file:
            try:
                id, name, age = [x.strip() for x in line.strip().split(',')]
                cats.append({'id': id, 'name': name, 'age': int(age)
                             })
            except ValueError:
                continue
    return cats

# Example usage:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

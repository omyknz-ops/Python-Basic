# Create a Python script that processes a log file and extracts specific information using functions, list comprehensions, and dictionary comprehensions.

import sys # For command-line arguments

def parse_log_line(line: str) -> dict: # Function to parse a single log line into a dictionary
    parts = line.split(" ")
    return {   
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': " ".join(parts[3:]) # Join the rest of the parts as the message
    }

# Function to load logs from a file and parse each line into a list of dictionaries
def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        logs = list(map(parse_log_line, (line.strip() for line in file))) # Using map and generator expression to parse each line
          
    return logs    


# Function to filter logs by a specific level using list comprehension
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level] # List comprehension to filter logs by level


# Function to count logs by level using a dictionary comprehension
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level'] # Extract the log level
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts


# Function to display log counts in a formatted table
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("------------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

# Main function to handle command-line arguments and execute the script logic
def main():
    if len(sys.argv) < 2:
        print(" Використання: python main.py <шлях_до_файлу> [рівень]")
        return
    file_path = sys.argv[1] # Get the file path from command-line arguments
    logs = load_logs(file_path)
    count = count_logs_by_level(logs)
    display_log_counts(count)
    if len(sys.argv) == 3:  # If a log level is provided, filter and display logs of that level
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nЛоги з рівнем '{level}':")
        for log in filtered_logs:
            print(f'{log['date']} {log['time']} {log['level']} {log['message']}')
    
if __name__ == "__main__": # Entry point for the script
    main() # Call the main function
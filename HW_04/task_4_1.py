
def total_salary(path): # define the function to calculate total and average salary
    total = 0 # initialize total salary starting from 0
    count = 0 # initialize count of valid salary entries 

    # open the file and read line by line
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                name, salary = line.strip().split(',') # split each line into name and salary, remove whitespace
                name = name.strip() # clean up name by stripping whitespace
                salary = salary.strip() # clean up salary by stripping whitespace
                salary = int(salary) # convert salary to integer
                total += salary # add salary to total
                count += 1 # increment count of valid salary entries
            except ValueError: # handle lines that do not conform to expected format
                continue
    if count == 0:  # avoid division by zero
        average = 0
    else:
        average = total // count # calculate average salary using integer division
    return total, average

# Example usage:  
total, average = total_salary('salary_test.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

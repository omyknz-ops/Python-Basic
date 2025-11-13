# calculate total income from text using generator and regex

import re # regular expressions module
from typing import Callable # for type hinting

# Generator function to extract numbers from text
def generator_numbers(text):
    numbers = re.findall(r'\b\d+\.?\d*\b', text) # regex to find integers and floats
    for number in numbers:
        yield float(number) # yield each number as float

# Function to sum up the numbers extracted by the generator
def sum_profit(text:str, func: Callable) -> float: 
    return sum(func(text)) # sum all numbers from the generator


# Example usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
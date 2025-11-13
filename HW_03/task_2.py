import random

def get_numbers_ticket(min, max,quantity): #generates a list of unique random numbers within a specified range and of a specified length
    if min < 1: #min value should be at least 1
        return [] #return empty list if min is less than 1
    if max > 1000: #max value should not exceed 1000
        return [] #return empty list if max is greater than 1000
    if quantity > (max - min + 1): #quantity should not exceed the range of numbers available
        return [] #return empty list if quantity is too large for the given range
    
    ticket = random.sample(range(min, max + 1), quantity) #generate unique random numbers
    ticket.sort() #sort the numbers in ascending order


    return ticket #return the sorted list of unique random numbers

from datetime import datetime, date, timedelta #import necessary modules 

#function to get upcoming birthdays within the next 7 days
def get_upcoming_birthdays(users): 
    today = date.today() #get today's date
    result = [] #list to store results
    
    #iterate through each user in the users list
    for user in users: 
        name = user['name'] 
        birthday_str = user['birthday'] 
        converted_birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date() #convert birthday string to date object in a correct format
        birthday_this_year = converted_birthday.replace(year=today.year) #set birthday to this year
        
        #if birthday has already occurred this year, set it to next year
        if birthday_this_year < today: 
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) 
        
        days_until_birthday = (birthday_this_year - today).days
        
            #check if birthday is within the next 7 days
        if 0 <= days_until_birthday <= 7: 
            weekday = birthday_this_year.weekday() 
            if weekday == 5: 
                congratulation_date = birthday_this_year + timedelta(days=2) 
            elif weekday == 6: 
                congratulation_date = birthday_this_year + timedelta(days=1) 
            else:
                congratulation_date = birthday_this_year 
            
            result.append ({
                'name': name, 
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
                }) #append name and congratulation date to result list
            
    return result

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.10.7"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

from datetime import datetime 

# Function to calculate the number of days from a given date to today
def get_days_from_today(date_string): 
    # Parse the input date string
    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date() # Convert string to date
        today = datetime.today().date() #Get today's date
        delta = today - given_date #Calculate the difference
        return delta.days #Return the difference in days 
    
    # Handle invalid date format
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
    
    # Example usage
print (get_days_from_today("2026-10-06")) # checking the function
print (get_days_from_today("2023-10-06")) # checking the function
print (get_days_from_today("13.14.2000")) # checking the function with invalid date format
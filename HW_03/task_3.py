import re #import regular expressions module 
def normalize_phone(phone_number): 
    
    # Remove all non-digit characters
   digits = re.sub(r'[^\d+]', '', phone_number) #remove [^\d] — all symbols, except digits and +
   clean = digits #assign cleaned digits to variable clean

   # Normalize to +international format
   if clean.startswith("+"): 
      return clean #if starts with +, keep it
   elif clean.startswith("380") and len(clean) == 12:
    return "+" + clean
   elif clean.startswith("+380") and len(clean) == 13: 
      return clean
   elif clean.startswith("0") and len(clean) == 10:
      return "+38" + clean
   elif clean.startswith("8") and len(clean) == 11:
    # 8XXXXXXXXXX → +38XXXXXXXXXX
    return "+3" + clean[1:]
   else:
      raise ValueError("Invalid phone number") #raise error if number is invalid
   
# Check using the example
phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "+421 952 009 200",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in phone_number] #list comprehension to apply normalize_phone to each number in phone_number list
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
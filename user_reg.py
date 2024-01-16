'''

@Author: Rohan Vetale

@Date: 2024-01-16 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-16 18:00:30

@Title : Program to use regex for pattern matching while user registration

''' 
import re

def first_name_check():
    #UC1
    user_input = input("Enter First name starts with Cap and has min. 3 characters ->")
    pattern = r'^[A-Z].+'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result


result = first_name_check()
if result:
    print('User has entered the first name correctly')
    


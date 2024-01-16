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
    user_input = input("Enter First name starts with Cap and has min. 3 characters -> ")
    pattern = r'^[A-Z].+'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result

def last_name_check():
    #UC2
    user_input = input("Enter Last name starts with Cap and has min. 3 characters -> ")
    pattern = r'^[A-Z].+'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result

def email_valid():
    #UC3
    user_input = input("Enter your valid email address completely -> ")
    pattern = r'^[\w.-]+@([\w-]+\.[\w.-]+)$'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result

def check_phone_num():
    #UC3
    #phone number should be country code and then space and then a 10 digit phone number that starts with 6-9
    user_input = input("Enter your country code and then space and your 10 digit phone number -> ")
    pattern = r'^\d{1,3}\s[6-9]\d{9}$'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result


result1 = first_name_check()
result2 = last_name_check()
result3 = email_valid()
result4 = check_phone_num()

if result1 :
    print('User has entered the first name correctly')
    
if result2 :
    print('User has entered the last name correctly')
    
if result3 :
    print('User has entered the email correctly')
    
if result4 :
    print('User has entered the phone number correctly')
    
    
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
    #UC4
    #phone number should be country code and then space and then a 10 digit phone number that starts with 6-9
    user_input = input("Enter your country code and then space and your 10 digit phone number -> ")
    pattern = r'^\d{1,3}\s[6-9]\d{9}$'
    result = False
    if len(user_input) > 2:
        result = re.match(pattern,user_input)
    return result

def check_password():
    #UC5 - UC8
    #Password should be min 8 char
    user_input = input("Enter your password of minimum 8 characters and with one uppercase character -> ")
    pattern = r'\w{8}'
    analaysis= "Invalid password"
    results = re.match(pattern,user_input)
    if results:
        analaysis = "Consist of 8 characters "
        #pattern should be consisting of atleast one character upper case
        pattern = r'[A-Z]'
        result2 = re.search(pattern,user_input)
        if result2:
            analaysis += " , has one or more upper case characters "
            #checking for atleast one numeric character
            pattern = r'[0-9]'
            result3 = re.search(pattern,user_input)
            if result3:
                analaysis += " , has one or more numeric character(s) "
                pattern = r'[!@#$%^&*()]{1}'
                result4 = re.search(pattern,user_input)
                if result4:
                    analaysis += " and has exactly one special character. "
                    #[!@#$%^&*()+]
                
            
    print(analaysis)
                
    

result_1 = first_name_check()
result_2 = last_name_check()
result_3 = email_valid()
result_4 = check_phone_num()
result_5 = check_password()


if result_1 :
    print('User has entered the first name correctly')
    
if result_2 :
    print('User has entered the last name correctly')
    
if result_3 :
    print('User has entered the email correctly')
    
if result_4 :
    print('User has entered the phone number correctly')
    
if result_5 :
    print('User has entered the password correctly')
    
    
    
    
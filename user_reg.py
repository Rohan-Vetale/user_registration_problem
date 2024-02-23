'''

@Author: Rohan Vetale

@Date: 2024-01-17 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-17 18:00:30

@Title : Program to use regex for pattern matching while user registration

''' 
import re

def first_name_check(user_input):
    #UC1
    """
    Description: This function checks for the first name validation
    Parameter: user_input : Input given by the user in string
    Return: Boolean value of whether first name is valid
    """
    
    pattern = r'^[A-Z].{2,}'
    
    result = re.match(pattern,user_input)
    if result:
        return True
    return False

def last_name_check(user_input):
    #UC2
    """
    Description: This function checks for the last name validation
    Parameter: user_input : string value of user input
    Return:Boolean value of whether last name is valid
    """
    pattern = r'^[A-Z].{2,}'
    
    result = re.match(pattern,user_input)
    if result:
        return True
    return False

def email_valid(user_input):
    #UC3
    """
    Description: This function checks for the email validation
    Parameter: user_input : string value of user input
    Return: Boolean value of whether email is valid
    """
    pattern = r'^[\w.-]+@([\w-]+\.[\w.-]+)$'
    
    result = re.match(pattern,user_input)
    if result:
        return True
    return False

def check_phone_num(user_input):
    #UC4
    #phone number should be country code and then space and then a 10 digit phone number that starts with 6-9
    """
    Description: This function checks for the phone number validation
    Parameter: user_input : string value of user input
    Return: Boolean value of whether phone number is valid
    """
    pattern = r'^\d{1,3}\s[6-9]\d{9}$'
    
    result = re.match(pattern,user_input)
    if result:
        return True
    return False

def check_password(user_input):
    #UC5 - UC8
    #Password should be min 8 char
    """
    Description: This function checks for the password validation
    Parameter: user_input : string value of user input
    Return: Boolean value of whether password is valid
    """
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
                pattern = r'^(?=(.*[!@#$%^&*()]){1})(?!(.*[!@#$%^&*()]){2})[a-zA-Z0-9!@#$%^&*()]*$'
                result4 = re.match(pattern, user_input)
                if result4:
                    analaysis += " and has exactly one special character. "
                    #r'(?=[!@#$%^&*()]*[!@#$%^&*()])(?!.*[!@#$%^&*()].*[!@#$%^&*()])^[!@#$%^&*()]+$'
                    return True
    return False
                
            
    
                
    
if __name__ == '__main__':
    result_1 = first_name_check("Rohan")
    result_2 = last_name_check("Vetale")
    result_3 = email_valid("vetalerohan@gmail.com")
    result_4 = check_phone_num("8356855555")
    result_5 = check_password("Rbv12803@")


    if result_1 :
        print('User has entered the first name correctly')
        
    if result_2 :
        print('User has entered the last name correctly')
        
    if result_3 :
        print('User has entered the email correctly')
        
    if result_4 :
        print('User has entered the phone number correctly')
    

    
    
    
    

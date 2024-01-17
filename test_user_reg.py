import pytest
import user_reg

def test_first_name_check():
    #check for user_input less than 3 characters
    result = user_reg.first_name_check("Ro")
    assert result == False
    #check for user_input more than 3 char but Not in A-Z
    result = user_reg.first_name_check("rohan")
    assert result == False
    #check for a valid user_input
    result = user_reg.first_name_check("Rohan")
    assert result == True
    
def test_last_name_check():
    #check for user_input less than 3 characters
    result = user_reg.last_name_check("Ve")
    assert result == False
    #check for user_input more than 3 char but Not in A-Z
    result = user_reg.last_name_check("vetale")
    assert result == False
    #check for a valid user_input
    result = user_reg.last_name_check("Vetale")
    assert result == True

# Test case for valid email
def test_email_valid():
    assert user_reg.email_valid('test@example.com') == True

# Test case for invalid email
def test_email_invalid():
    assert user_reg.email_valid('invalid-email') == False

# Test case for email with less than 3 characters
def test_email_short():
    assert user_reg.email_valid('a@b') == False

# Test case for email with exactly 3 characters
def test_email_exact_length():
    assert user_reg.email_valid('abc') == False

# Test case for email with more than 3 characters
def test_email_long():
    assert user_reg.email_valid('longemail@example.com') == True

# Test case for email with special characters
def test_email_special_characters():
    assert user_reg.email_valid('user.name@example.co.uk') == True
    
# Test case for valid phone number
def test_valid_phone_num():
    assert user_reg.check_phone_num('91 9876543210') == True

# Test case for invalid phone number (less than 10 digits)
def test_short_phone_num():
    assert user_reg.check_phone_num('91 123456789') == False

# Test case for invalid phone number (more than 10 digits)
def test_long_phone_num():
    assert user_reg.check_phone_num('91 987654321012') == False

# Test case for invalid phone number (does not start with 6-9)
def test_invalid_start_digit():
    assert user_reg.check_phone_num('91 0123456789') == False

# Test case for invalid phone number (missing space after country code)
def test_missing_space():
    assert user_reg.check_phone_num('919876543210') == False

# Test case for invalid phone number (non-numeric characters)
def test_non_numeric_chars():
    assert user_reg.check_phone_num('91 abcdefghij') == False
    
# Test case for valid password
def test_valid_password():
    assert user_reg.check_password('Abcdefg1!') == True

# Test case for invalid password (less than 8 characters)
def test_short_password():
    assert user_reg.check_password('Abc123!') == False

# Test case for invalid password (missing uppercase character)
def test_missing_uppercase():
    assert user_reg.check_password('abcdefg1!') == False

# Test case for invalid password (missing numeric character)
def test_missing_numeric():
    assert user_reg.check_password('Abcdefgh!') == False

# Test case for invalid password (missing special character)
def test_missing_special_char():
    assert user_reg.check_password('Abcdefg12') == False

# Test case for invalid password (more than one special character)
def test_extra_special_chars():
    assert user_reg.check_password('Abcdefg1!!') == False

# Test case for invalid password (no alphabetic characters)
def test_no_alphabetic_chars():
    assert user_reg.check_password('12345678!') == False
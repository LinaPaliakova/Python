import re
def strong_password_checker(password):
    password = str(password)
    is_strong = False
    if len(password) < 8:
        print('The password must be at least 8 characters long.')
        is_strong = False
    regex_lowercases = re.compile(r'[a-z]+')
    password_lowercase = re.search(regex_lowercases, password)
    if password_lowercase == None:
        print('The password must include at least 1 lowercase.')
        is_strong = False
    regex_uppercase = re.compile(r'[A-Z]+') 
    password_uppercase = re.search(regex_uppercase, password) 
    if password_uppercase == None:
        print('The password must include at least 1 uppercase.')
        is_strong = False
    regex_digits = re.compile(r'\d+')
    password_digits = re.search(regex_digits, password) 
    if password_digits == None:
        print('The password must include at least 1 digit.')
        is_strong = False
    regex_special_char = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    password_special_char = re.search(regex_special_char, password)
    if password_special_char == None:
        print ('The password must include at least 1 special character.')
        is_strong = False
    if  is_strong == True:   
        print('Your password is strong')

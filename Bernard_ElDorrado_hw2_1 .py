#  coding: utf-8 -*-
"""
@author: Bernard M. ElDorrado Sr.

Problem Number 1
Write a program that accepts a password from a user

"""
def password():
    
    pwd = input('Enter your password: ')
    len_pwd = len(pwd)
     
    x = True
    
    if len_pwd < 9:
        print(pwd, 'is less than 9 characters')
        x = False
    

    if pwd.isalnum() == False:
            print(pwd, 'contains non-alphanumeric character') 
            x = False
            
    
    if len(pwd) > 1:
        if pwd[1].isnumeric() == False:
            print('The second character ', pwd[1], 'is not numeric')
            x = False     
        
            
    if pwd[-1].isalpha() == False:
        print('The last character ', pwd[-1], ' must be an alpha character')
        x = False
    
    if x == False:
        print('Your password is', pwd, ', Please try again')
    else:    
        print('Congratulations, password meets all the criteria.')   
        
password()


"""
Enter your password: d
d is less than 9 characters
Your password is d , Please try again

password()


Enter your password: dd
dd is less than 9 characters
The second character  d is not numeric
Your password is dd , Please try again

password()


Enter your password: 1234567890
The last character  0  must be an alpha character
Your password is 1234567890 , Please try again

password()

Enter your password: 1234457wsxBB
Congratulations, password meets all the criteria.

password()


Enter your password: 12345678()
12345678() contains non-alphanumeric character
The last character  )  must be an alpha character
Your password is 12345678() , Please try again

 password()


Enter your password: $%
$% is less than 9 characters
$% contains non-alphanumeric character
The second character  % is not numeric
The last character  %  must be an alpha character
Your password is $% , Please try again

"""

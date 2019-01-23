#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Bernard M. ElDorrado Sr.

Problem Number 2
Write a Python program to build a simple "English language" calculator

""" 

def calculator():
    numbers = ('zero','one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine')
   
    myCalc = input('Enter three or four characters for your calculations: ')    
    
    char_count = len(myCalc)
    error_code = False
    
    if myCalc[0] in valid_input == False:
        print('Please use numbers and operators +,-,/.*,**')
    else:
        if char_count < 3 or char_count > 4:
            print('Please use 3 or 4 characters')
            error_code = True
        else: 
            if myCalc[0].isnumeric() == False or myCalc[-1].isnumeric() == False:
                print('Please enter a numeric values in the first and last positions')
                error_code = True
            else:
                if char_count == 3:
                    num1 = eval(myCalc[0])
                    operation = myCalc[1]
                    num2 = eval(myCalc[2])
                    if operation == "+":
                        answer = num1 + num2
                        symbol = 'plus'
                    if operation == "-":
                        answer = num1 - num2
                        symbol = 'minus'
                    if operation == "*":
                        answer = num1 * num2
                        symbol = 'multiplied by'
                    if operation == "/":
                        if num2 == 0:
                          print('Division by 0 is not allowed')
                          error_code = True
                        else:
                            answer = num1 / num2
                            symbol = 'divided by'
                else:
                    if myCalc[1] == '*' and myCalc[2] == '*':
                        num1 = eval(myCalc[0])
                        num2 = eval(myCalc[3])
                        answer = num1 ** num2
                        symbol = 'to the power of'
                    else:
                        print('Use "**" for the exponential calculation in position 2 and 3')
                        error_code = True
        if error_code == False:            
            print('The answer to your calculation is: ', numbers[num1], ' ', symbol, ' ', numbers[num2], ' = ', answer)
        else:
            print('There are errors in the input received from the calculator')
            
calculator()

"""
calculator()

Enter three or four characters for your calculations: 44444

Please use 3 or 4 characters
There are errors in the input received from the calculator

calculator()

Enter three or four characters for your calculations: 7*7

The answer to your calculation is:  seven   multiplied by   seven  =  49

calculator()

Enter three or four characters for your calculations: 3/0

Division by 0 is not allowed
There are errors in the input received from the calculator

calculator()

Enter three or four characters for your calculations: 2**8

The answer to your calculation is:  two   to the power of   eight  =  256

                    
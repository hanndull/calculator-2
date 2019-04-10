"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def evaluate_input(calcinput):

    prefix = calcinput[0]
    if prefix == "q":
        return "q"
    if len(calcinput) == 2:
        calcinput1 = float(calcinput[1])  

    elif len(calcinput) == 3:    
        calcinput1 = float(calcinput[1])
        calcinput2 = float(calcinput[2])
        
    if prefix == '+':
        return add(calcinput1, calcinput2)
    elif prefix == "-":
        return subtract(calcinput1, calcinput2)
    elif prefix == "*":
        return multiply(calcinput1, calcinput2)
    elif prefix == "/":
        return divide(calcinput1, calcinput2)
    elif prefix == "square":
        return square(calcinput1)
    elif prefix == "cube":
        return cube(calcinput1)
    elif prefix == "pow":
        return power(calcinput1, calcinput2)
    elif prefix == "mod":
        return mod(calcinput1, calcinput2)    






# Your code goes here

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token


while True:
    calcinput = input()
    calcinput = calcinput.split()
    output = evaluate_input(calcinput) 
    if output == "q":
        break
    print(output)

     #TODO: Need to build out this function 


    


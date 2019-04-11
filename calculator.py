"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce

def evaluate_input(calcinput):
    """evaluates user input and calls appropriate arithmetic function"""
    prefix = calcinput[0]
    
    if prefix == "q":
        return "q"

    arguments = calcinput[1:]
    array = []

    for argument in arguments:
        array.append(float(argument))
    # print(array,"this is working")    
        
  
    
    # if len(calcinput) == 2:
    #     calcinput1 = float(calcinput[1])  

    # elif len(calcinput) >= 3:    
    #     calcinput1 = float(calcinput[1])
    #     calcinput2 = float(calcinput[2])
            

        
    if prefix == '+':
        return reduce(add,array)
      
    elif prefix == "-":
        return reduce(subtract,array)
    
    elif prefix == "*":
        return reduce(multiply, array)
    
    elif prefix == "/":
        return reduce(divide, array)
    
    elif prefix == "square":
        return reduce(square, array)
    
    elif prefix == "cube":
        return reduce(cube, array)
    
    elif prefix == "pow":
        return reduce(power, array)
    
    elif prefix == "mod":
        return reduce(mod, array)    






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
    #print(*calcinput)
   
    output = evaluate_input(calcinput) 
    if output == "q":
        break
    if output == None:
        print("thats..... not right!")
    else:        
        print(output)

     #TODO: Need to build out this function 


    


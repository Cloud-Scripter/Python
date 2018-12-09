#Every string should have + & = operator. Each character should be surrounded by + symbol. +a+b+c+=0 is correct, ab+=cd is wrong.

import sys

def SimpleSymbols(str): 
    if len(str) < 3:
        return False   
    if "+" not in str:
        return False
    
    i = len(str)-1
    while i > 0:
        if str[i].isalpha():
            if i == 0 or i == len(str)-1:
                return False
            if (str[i-1] != "+" ) or (str[i+1] != "+" ):
                return False

        i = i-1 
    # code goes here 
    return True
    
# keep this function call here  
print(SimpleSymbols(input()))
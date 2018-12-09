import sys

def reverse(s):
    str = ""
    for i in s:
        str = str + i 
    return str


userInput = str(input('Enter String: '))
print(reverse(userInput))
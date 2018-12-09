import sys

def Factorial(num):
    result = 1
    while(num > 1):
        result = result * (num)
        num = num - 1
    return result

user_input = input("Enter Number : ")
print(Factorial(user_input))
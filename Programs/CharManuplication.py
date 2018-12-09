import sys

def LetterChanges(str): 
    temp = ""
    output = ""
    for i in str:
        
        if ord(i)>97 and ord(i)<=122:
            #conver to lower character
            if(ord(i)== 122):
                temp = "A"
            else:
                temp = chr(ord(i) + 1)
        
            # Conver to Vovels to Capital
            if temp in ['a','e','i','o','u']:
                temp = temp.upper()

        else:
            temp = i 
        output = output + temp

    return output

print(LetterChanges("fun times!"))

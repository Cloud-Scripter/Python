def sortString(str): 
    strList = list(str)
    length = len(str)
    for i in range(0,length):
        for j in range(i,length):
            temp = strList[i]
            if strList[j] < strList[i]:
                #Swap
                temp = strList[i]
                strList[i]=strList[j]
                strList[j]=temp

            j = j + 1
        i = i + 1
    return ''.join(strList)

def distinctString(str):
    global strList
    strList = list(str)
    distList = list()

    for i in range(0,len(str)):
        if strList[i] not in distList:
            distList.append(strList[i])

    return ''.join(distList)

print(distinctString("Tanmay   Tanmay"))


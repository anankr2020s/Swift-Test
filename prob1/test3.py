def factNumber(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

def countZero(n):
    factValue = factNumber(n)
    newList = []
    newList[:0] = str(factValue)
    maxLength = len(newList)
    haveZero = 0
    while(maxLength > 0):
        if(newList[maxLength-1] in '0'):
            haveZero+=1
        else :
            return haveZero
        maxLength-=1
    return haveZero

        
print(countZero(10))


def maxIndexValue(arr):
    maxLength = len(arr)
    i = 0
    maxValue = 0
    maxIndex = 0
    while(i<maxLength):
        if(arr[i] >= maxValue):
            maxValue = arr[i]
            maxIndex = i
        i+=1
    return maxIndex
print(maxIndexValue([1,2,1,3,5,6,4]))

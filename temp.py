def ReadData():
    arr = []
    with open("Data.txt", 'r') as f:
        for line in f:
            arr.append(line.strip())
    return arr

def FormatArray(arr):
    temp = ""
    for i in arr:
        temp = temp + str(i) + " "
    print(temp)

array = ReadData()
FormatArray(array)

def CompareStrings(str, str1):
    for i, j in zip(str, str1):
        if i < j:
            return "1"
        elif i > j:
            return "2"
        else:
            continue
    return "0"

def Bubble(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
                
    return arr

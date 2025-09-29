sample = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

def findMinMax(arr: list):
    length = len(arr)

    if(length == 1):
        return arr[0], arr[0]
    
    if(length == 2):
        return (arr[0], arr[1   ]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    mid = length // 2
    minLeft, maxLeft = findMinMax(arr[:mid])
    minRight, maxRight = findMinMax(arr[mid:])

    min = minLeft if minLeft < minRight else minRight
    max = maxLeft if maxLeft > maxRight else maxRight

    return min, max

resultMin, resultMax = findMinMax(sample)
print(resultMin, resultMax)

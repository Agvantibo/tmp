input()
arr = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]

def binaryGet(arr, x): 
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        else: 
            return mid
    return -1
for i in queries:
    randomElementIndex = binaryGet(arr, i)
    lastElementIndex = randomElementIndex
    firstElementIndex = randomElementIndex
    try:
        nextIndex = arr[randomElementIndex + 1]
    except IndexError:
        nextIndex = ''
    try:
        previousIndex = arr[randomElementIndex - 1]
    except IndexError:
        previousIndex = ''
    if nextIndex == i:
        for j in range(randomElementIndex, len(arr) - 1):
            if j != i:
                break
            lastElementIndex += 1
    if previousIndex == i:
        for j in range(0, randomElementIndex, -1):
            if j != i:
                break
            lastElementIndex -= 1
    if randomElementIndex == -1:
        print(0)
    else:
        print(firstElementIndex + 1, lastElementIndex + 1)

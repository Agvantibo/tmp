input()
array = [int(i) for i in input().split()]
biggest = array[0]
for i in array:
    if i > biggest:
        biggest = i
print(array.index(biggest) + 1)

input()
array = [int(i) for i in input().split()]
biggest = array[1]
for i in array:
    if i > biggest:
        biggest = i
print(biggest)

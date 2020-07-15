input()
array = [int(i) for i in input().split()]
biggest = array[0]
biggest_index = 0
for i in range(1, len(array) - 1):
    if i > biggest:
        biggest_index = i
        biggest = array[i]
print(biggest_index + 1)

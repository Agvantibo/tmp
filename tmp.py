class flist():

    def __init__(self, arr):
        self.arr = arr
    

    def swap(self, i1, i2):
        buffer = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = buffer


input()
array = flist([int(i) for i in input().split()])

array.arr.sort()

print(' '.join(map(str, array.arr)))

input()
ar1 = [int(i) for i in input().split()]

if len(ar1) > 0:
    b_ind = 0
    valBuf = ar1[b_ind]

    for i in range(1, len(ar1) - 1):
            if valBuf < ar1[i]:
                b_ind = i
                valBuf = ar1[i]

    print(valBuf+1)
else:
    print ("error")

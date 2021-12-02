n = int(input())
dip = list(map(int, input().split()))

if len(dip) == 2:
    j = 1
else:
    j = 0
    dip.sort()

    for i in range(len(dip)):
        if i == len(dip) - 1:
            break
        j += dip[i]


print(j)

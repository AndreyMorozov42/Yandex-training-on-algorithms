n = int(input())
mxn = n
i = 1
while n != 0:
    n = int(input())
    if mxn < n:
        i = 1
        mxn = n
    elif mxn == n:
        i += 1
print(i)
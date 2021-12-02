num = list(map(int, input().split()))
d = dict()
d = d.fromkeys(num, 0)

for i in range(len(num)):
    d[num[i]] += 1

for i in d:
    if d[i] == 1:
        print(i, end=' ')

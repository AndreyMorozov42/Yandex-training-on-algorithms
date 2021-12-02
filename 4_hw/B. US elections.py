d = dict()
f = set()
ch = list(map(str, input().split('\n')))
while ch != []:
    if ch[0] in d:
        d[ch[0]] += int(ch[1])
    else:
        d[ch[0]] = int(ch[1])
        f.add(ch[0])
    ch = list(map(str, input().split()))

f = list(f)
f.sort()

for i in f:
    print(i, d[i])

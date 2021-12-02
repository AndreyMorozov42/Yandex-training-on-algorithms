n = int(input())
voc = {}

for i in range(n):
    d, a = map(int, input().split())

    if d in voc:
        x = voc.get(d) + a
        voc[d] = x
    else:
        voc[d] = a

list_k = list(voc.keys())
list_k.sort()

for i in list_k:
    print(i, voc[i])


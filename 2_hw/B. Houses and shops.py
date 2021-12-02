n = [int(i) for i in input().split()]
shops = list()
dist = list()

for i in range(len(n)):
    if n[i] == 2:
        shops.append(i)

for i in range(len(n)):
    if n[i] == 1:
        shops.append(i)
        shops.sort()
        ind = shops.index(i)
        if ind == 0:
            dist.append(shops[ind + 1] - shops[ind])
        elif ind == len(shops) - 1:
            dist.append(shops[ind] - shops[ind - 1])
        else:
            x1 = shops[ind] - shops[ind - 1]
            x2 = shops[ind + 1] - shops[ind]
            if x1 < x2:
                dist.append(x1)
            else:
                dist.append(x2)
        shops.pop(ind)
print(max(dist))





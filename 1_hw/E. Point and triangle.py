def dist(x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5


d = int(input())
x, y = map(int, input().split())

xa, ya = 0, 0
xb, yb = d, 0
xc, yc = 0, d

a = (xa - x) * (yb - ya) - (xb - xa) * (ya - y)
b = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
c = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)

if a >= 0 and b >= 0 and c >= 0:
    print(0)
else:
    da = dist(x, y, xa, ya)
    db = dist(x, y, xb, yb)
    dc = dist(x, y, xc, yc)
    if da == db and da == dc:
        print(1)
    elif da <= db and da <= dc:
        print(1)
    elif db < da and db <= dc:
        print(2)
    elif dc < da and dc < db:
        print(3)
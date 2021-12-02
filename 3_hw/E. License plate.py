n = int(input())
set_el = set()

for i in range(n):
    s = set([i for i in input()])
    set_el.update(s)

m = int(input())

for i in range(m):
    s = input()
    lis = set([i for i in s])



num = map(int, input().split())
s = set()

for i in num:
    if i in s:
        print('YES')
    else:
        print('NO')
    s.add(i)
        
        

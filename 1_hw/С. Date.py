a, b, c = map(int, input().split())

if a <= 12 and b <= 12:
    if a == b:
        print(1)
    else:
        print(0)
else:
    print(1)
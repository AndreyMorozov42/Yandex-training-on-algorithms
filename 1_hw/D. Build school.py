a = int(input())
num = [int(i) for i in input().split()]

if a % 2 != 0:
    print(num[a // 2])
else:
    print((num[a // 2] + num[a // 2 - 1]) // 2)
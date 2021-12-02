s = input()
s_r = s[::-1]
cost = 0

if len(s) == 1:
    print(cost)
else:
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            if s[i] != s_r[i]:
                cost += 1
    elif len(s) % 2 != 0:
        for i in range(len(s) // 2):
            if s[i] != s_r[i]:
                cost += 1
    print(cost)
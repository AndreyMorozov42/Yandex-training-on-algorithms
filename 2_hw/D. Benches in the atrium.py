l, n = map(int, input().split())
x = list(map(int, input().split()))

lhs_mid = -1
rhs_mid = -1

if l % 2 == 0:
    lhs_mid = l // 2 + 1
    rhs_mid = l // 2
else:
    lhs_mid = rhs_mid = l // 2

left = 0
right = n - 1

while left < right:
    m = (right + left) // 2
    val = x[m]
    if val >= lhs_mid:
        right = m
    else:
        left = m + 1

if len(x) == 1:
    print(x[0])
elif rhs_mid == lhs_mid == x[left]:
    print(x[left])
else:
    print(x[left - 1], x[right])

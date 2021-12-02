N, i, j = map(int, input().split())

dist_ij_1 = abs(j - i) - 1

if (N - i) < (N - j):
    j += N
else:
    i, j = j, i
    j += N

dist_ij_2 = abs(j - i) - 1

if dist_ij_2 < dist_ij_1:
    print(dist_ij_2)
else:
    print(dist_ij_1)
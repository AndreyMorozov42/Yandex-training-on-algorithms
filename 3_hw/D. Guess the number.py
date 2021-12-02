num_max = int(input())
true_num = set(range(1, num_max + 1))

num = set([int(i) for i in input().split()])
say = input()

if say == 'YES':
    true_num &= num
elif say == 'NO':
    true_num -= num
 


while say != 'HELP':
    say = input()
    if say != 'HELP':
        num = [int(i) for i in say.split()]
        say = input()
        if say == 'YES':
            true_num &= set(num)
        elif say == 'NO':
            true_num -= set(num)

print(*sorted(true_num))

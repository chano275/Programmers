tc = int(input())

for qqq in range(1, tc + 1):
    a = list(map(int, input().split()))
    max_a = max(a)

    temp_sum = 0
    for i in range(3):
        if a[i] == max_a:continue
        temp_sum += a[i] ** 2

    print(f'Scenario #{qqq}:')
    if max_a ** 2 == temp_sum:
        print('yes')
    else:
        print('no')

    print('')
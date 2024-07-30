num_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    number = (input())

    four_numbers = set()
    loop = n // 4

    for _ in range(loop):
        # print(number)
        for i in range(4):
            four_numbers.add(number[i * loop : (i + 1) * loop])
        # 0 ~ 9 + A ~ F
        number = number[-1] + number[0:len(number) - 1]

    four_numbers = list(four_numbers)

    for check_num in range(len(four_numbers)):
#        print(check_num)
        rev = four_numbers[check_num][::-1]
#        print('*****************')
#        print(rev)
        sum_temp = 0
        for j in range(len(rev)):
#            print(j, rev[j])
            # print(sum_temp)
            if 'A' <= rev[j] <= 'Z':  sum_temp += (16 ** j) * num_dict[rev[j]]
            else:  sum_temp += (16 ** j) * int(rev[j])
#            print(sum_temp)
        four_numbers[check_num] = sum_temp
#        print('*****************')
    # print(check_num)

    four_numbers.sort(reverse=True)
    print(f'#{tc} {four_numbers[k-1]}')

#        print(zar)
#    print(list(four_numbers))
#    numberstep = n/4


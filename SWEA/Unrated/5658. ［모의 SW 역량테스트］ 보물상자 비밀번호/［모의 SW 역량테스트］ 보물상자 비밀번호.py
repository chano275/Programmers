T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    number = input()

    number_set = set()

    leng = n//4

    for _ in range(n):
        for i in range(leng):
            number_set.add(number[leng * i : leng * (i+1)])
        number = number[1:n] + number[0]

    number_set = list(number_set)

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    chars = []
    lineup = []

    for _str in number_set:
        temp_sum = 0
        str_ = _str[::-1]
        for j in range(len(_str)): # j : 0 1 2
            if (str_[j]) in numbers:
                temp_sum += 16**j * int(str_[j])  # 숫자 :

            else:  # 영어
                if str_[j] == 'A':temp_sum += 16**j * 10
                elif str_[j] == 'B':temp_sum += 16**j * 11
                elif str_[j] == 'C':temp_sum += 16**j * 12
                elif str_[j] == 'D':temp_sum += 16**j * 13
                elif str_[j] == 'E':temp_sum += 16**j * 14
                elif str_[j] == 'F':temp_sum += 16**j * 15

        lineup.append(temp_sum)

    # print(lineup)

    lineup.sort(reverse=True)

    print(f'#{tc} {lineup[k-1]}')
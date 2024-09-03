def dfs(num, idx):
    # print(num, idx)
    global answer
    if idx == s_count:  # 교환횟수 다 사용
        temp_num = int(''.join(num))
        answer = max(answer, temp_num)

        return

    for i in range(len(number) - 1):
        for j in range(i+1, len(number)):
            if i == j:continue

            num[i], num[j] = num[j], num[i]
            temp_num = int(''.join(num))
            if (temp_num, idx) in global_set:
                num[j], num[i] = num[i], num[j]
                continue
            else:
                dfs(num, idx + 1)
                global_set.add((temp_num, idx))
                num[j], num[i] = num[i], num[j]

    return


T = int(input())
for tc in range(1, T+1):
    n, s_count = map(int, input().split())
    number = []
    for s in str(n):        number.append(s)

    answer = 0
    global_set = set()
    dfs(number, 0)
    print(f'#{tc} {answer}')
def dfs(arr, idx, cur):
    if idx == n-1 or len(cur) == n - 1:
        if len(cur) == n - 1:
            oppo_set.add(cur)
        return

    for i in range(4):
        if arr[i] != 0:
            _arr = arr[:]
            _arr[i] -= 1
            dfs(_arr, idx + 1, cur + operators[i])

    return


operators = ['+', '-', '*', '/']
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    oppo_numbers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    oppo_set = set()

    dfs(oppo_numbers, 0, '')
    oppo_list = list(oppo_set)

    ans_min, ans_max = float('inf'), -1 * float('inf')


    for str_operator in oppo_list:
        temp = numbers[0]
        cnt = 1
        for oper in str_operator:
            if oper == '+':temp = temp + numbers[cnt]
            elif oper == '-':temp = temp - numbers[cnt]
            elif oper == '*':temp = temp * numbers[cnt]
            elif oper == '/':temp = int(temp / numbers[cnt])
            cnt += 1
        ans_min, ans_max = min(ans_min, temp), max(ans_max, temp)

    print(f'#{tc} {ans_max - ans_min}')


    # break
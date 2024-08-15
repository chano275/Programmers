# import sys
# sys.stdin = open('sample_input (8).txt')


def dfs(arr, idx, cur):
    if len(cur) == n-1 or idx == n:
        operator_set.add(cur)
        return

    for i in range(4):
        if arr[i] != 0:
            temp_arr1 = arr[:]
            temp_arr1[i] -= 1
            dfs(temp_arr1, idx + 1, cur + operator[i])


def calculate(front_num, opera, final_num):
    if opera == '+':return front_num + final_num
    elif opera == '-':return front_num - final_num
    elif opera == '*':return front_num * final_num
    elif opera == '/':return int(front_num / final_num)



T = int(input())
operator = ['+', '-', '*', '/']
for tc in range(1, T+1):
    n = int(input())
    operator_list = list(map(int, input().split()))  # + - * /
    numbers = list(map(int, input().split()))

    operator_set = set()
    dfs(operator_list, 0, '')

    # numbers 는 그대로 / set list 만 다르게
    # // 같은 경우에 -가 나오면 내림 연산이 되므로, / 후 int 연산 진행

    ans_max, ans_min = -float('inf'), float('inf')
    for chk in list(operator_set):
        temp = numbers[0]
        numbers_cnt = 0
        for op in chk:
            numbers_cnt += 1
            temp = calculate(temp, op, numbers[numbers_cnt])
        ans_max, ans_min = max(ans_max, temp), min(ans_min, temp)

    print(f'#{tc} {ans_max - ans_min}')
    
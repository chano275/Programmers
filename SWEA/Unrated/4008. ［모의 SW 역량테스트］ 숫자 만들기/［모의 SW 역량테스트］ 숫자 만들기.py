def operate(a, _op, b):
    if _op == '+': return a+b
    elif _op == '-': return a-b
    elif _op == '*': return a*b
    elif _op == '/': return int(a/b)


def dfs(arr_str, op_val):
    if len(arr_str) == sum(op):
        perm_set.add(arr_str)
        return

    if op_val[0] > 0:
        _op = op_val[:]
        _op[0] -= 1
        dfs(arr_str + operator[0], _op)

    if op_val[1] > 0:
        _op = op_val[:]
        _op[1] -= 1
        dfs(arr_str + operator[1], _op)

    if op_val[2] > 0:
        _op = op_val[:]
        _op[2] -= 1
        dfs(arr_str + operator[2], _op)

    if op_val[3] > 0:
        _op = op_val[:]
        _op[3] -= 1
        dfs(arr_str + operator[3], _op)


T = int(input())
operator = ['+', '-', '*', '/']


for tc in range(1, T+1):
    n = int(input())  # 숫자 갯수
    op = list(map(int, input().split()))  # 연산자 배열 ( 갯수 : n - 1 )
    numbers = list(map(int, input().split()))  # 숫자 배열
    max_op, min_op = -float('inf'), float('inf')
    perm_set = set()

    #print(op)

    dfs('', op)

    #print(perm_set)

    change_to_list = list(perm_set)

    op_list = []

    for chk in change_to_list:
        temp = []
        for inp in chk:
            temp.append(inp)
        op_list.append(temp)

    for op_i in op_list:
        temp = numbers[0]
        _i = 1
        for do in op_i:
            temp = operate(temp, do, numbers[_i])
            _i += 1
        max_op = max(max_op, temp)
        min_op = min(min_op, temp)

    ans = max_op - min_op
    print(f'#{tc} {ans}')

    #break
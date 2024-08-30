def dfs(visited, cur):

    if operator_num == [0,0,0,0]:
        operator.append(cur)

    for i in range(4):
        if visited[i] != 0:
            visited[i] -= 1
            dfs(visited, cur + [op[i]])
            visited[i] += 1


n = int(input())
op = ['+', '-', '*', '/']

a_list = list(map(int, input().split()))
min_ans, max_ans = float('inf'), -float('inf')

operator_num = list(map(int, input().split()))  # + - * //
operator = []

dfs(operator_num, [])


for o in operator:
    cnt = 1
    temp = a_list[0]

    for i in o:
        if i == '+':temp += a_list[cnt]
        elif i == '-':temp -= a_list[cnt]
        elif i == '*':temp *= a_list[cnt]
        else:         temp = int(temp / a_list[cnt])
        cnt += 1

#    print(o, temp)

    min_ans = min(min_ans, temp)
    max_ans = max(max_ans, temp)

print(max_ans)
print(min_ans)
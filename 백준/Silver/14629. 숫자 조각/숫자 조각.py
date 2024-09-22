def dfs(str_num, v):
    global ans
    global print_ans

    diff = abs(n - int(str_num))
    if diff == 0:
        return n

    if ans == diff:
        print_ans = min(print_ans, int(str_num))

    else:
        if ans != min(ans, diff):
            ans = min(ans, diff)
            print_ans = int(str_num)

    for j in range(10):
        if v[j]:continue
        else:
            v[j] = True
            dfs(str_num + str(j), v)
            v[j] = False

    return


n = int(input())
ans, print_ans = float('inf'), 0
visited = [False] * 10

flag = 0

for i in range(1, 10):  # 맨 앞자리 +-1만 보는게 맞는거같은데
    # if i < int(str(n)[0]) - 1 or i > int(str(n)[0]) + 1:continue  # 987 1000 못잡음
    visited[i] = True

    if dfs(str(i), visited) == n:
        flag = 1
        break 

    visited[i] = False

if flag == 1: print(n)
else: print(print_ans)
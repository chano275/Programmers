dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(checker, x, y, memo, str_):
    if len(str_) == 7:
        memo.append(str_)
        return

    if 0 <= x < 4 and 0 <= y < 4:
        str_ += str(checker[x][y])
        for chk in range(4):
            if 0 <= x + dx[chk] < 4 and 0 <= y + dy[chk] < 4:
                dfs(checker, x + dx[chk], y + dy[chk], memo, str_)


T = int(input())
for test_case in range(1, T + 1):
    checker = []
    for _ in range(4):
        checker.append(list(map(int, input().split())))

    memo = []  # str_ 7 되었을 때에 넣을 memo list
    str_ = ''

    for i in range(4):
        for j in range(4):
            dfs(checker.copy(), i, j, memo, str_)

    print(f'#{test_case} {len(set(memo))}')
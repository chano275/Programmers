def garo(x):
    temp_set = number_set.copy()
    for i in range(9):
        if maps[x][i] != '0':
            temp_set.discard(maps[x][i])
    return temp_set


def sero(y):
    temp_set = number_set.copy()
    for i in range(9):
        if maps[i][y] != '0':
            temp_set.discard(maps[i][y])
    return temp_set


def square(cur_xy):
    temp_set = number_set.copy()
    x, y = cur_xy
    for p in range(x // 3 * 3, x // 3 * 3 + 3):
        for q in range(y // 3 * 3, y // 3 * 3 + 3):
            if maps[p][q] != '0':
                temp_set.discard(maps[p][q])
    return temp_set


def dfs(index):
    if index == len(zero_list):
        for row in maps:
            print(''.join(row))  # 한 줄씩 붙여서 출력
        exit()

    cx, cy = zero_list[index]
    possible_numbers = list(square((cx, cy)) & sero(cy) & garo(cx))

    for number in possible_numbers:
        maps[cx][cy] = number
        dfs(index + 1)
        maps[cx][cy] = '0'  # 백트래킹


maps = [list(input()) for _ in range(9)]
number_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

# 빈칸 좌표 리스트 생성
zero_list = [(i, j) for i in range(9) for j in range(9) if maps[i][j] == '0']

dfs(0)

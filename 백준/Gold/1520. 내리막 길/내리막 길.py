import sys
sys.setrecursionlimit(100000)


def dfs(cxy):
    cx, cy = cxy

    if cx == m-1 and cy == n-1:
        cnt_list[cx][cy] += 1
        return True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
        if maps[cx][cy] <= maps[nx][ny]: continue
        if cnt_list[nx][ny] == -1: continue
        if cnt_list[nx][ny] != 0:
            cnt_list[cx][cy] += cnt_list[nx][ny]
            continue

        tf = dfs((nx, ny))

        if tf:  cnt_list[cx][cy] += cnt_list[nx][ny]


    if cnt_list[cx][cy] != 0:
        return True
    else:
        if cx == 0 and cy == 0:
            cnt_list[0][0] = 0
            return
        cnt_list[cx][cy] = -1
        return False


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
m, n = map(int, input().split())  # m 행 / n 열
maps = [list(map(int, input().split())) for _ in range(m)]
cnt_list = [[0] * n for _ in range(m)]

# 여기서 잘 못됨 안가본칸도 0 / 갈길이 없는 칸도 0 어케구분???? 이거만 하면 끝

dfs((0, 0))

print(cnt_list[0][0])


"""
등산로 : 가장 높은 봉우리에서 시작 ( 여러곳 가능 )
높은 지형에서 낮은 지형으로 가로 / 세로 연결 ( 같은곳 / 높은곳 / 대각선 X )
* 긴 등산로 만들기 위해 한곳 정해서 [ 최대 K ]만큼 높이 - 가능

현재 있는 곳보다 무조건 -1 하는 k가 best ( k의 범위가 이걸 못하면, pass )
flag 는 그대로 사용

"""


def dfs(arr, sx, sy, flag, length):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌
    global ans

    # 들어온 위치 저장 / 방문 찍기
    cx, cy = sx, sy
    visited[cx][cy] = True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        # 범위 벗어나거나 방문했었으면 out
        # 다음 갈곳이 원래 못가는곳인데, 자르지도 못해? out
        if nx < 0 or nx >= n or ny < 0 or ny >= n:continue
        if visited[nx][ny]:continue
        if flag == 0 and arr[nx][ny] >= arr[cx][cy]:continue

        # 다음 갈곳이 원래 못가는곳인데, 자를 수 있어?
        if flag == 1 and arr[nx][ny] >= arr[cx][cy]:
            if arr[nx][ny] - k <= arr[cx][cy] - 1:
                throw = []
                for ctc in arr: throw.append(ctc[:])
                throw[nx][ny] = throw[cx][cy] - 1
                dfs(throw, nx, ny, 0, length + 1)
            continue

        dfs(arr, nx, ny, flag, length + 1)

    ans = max(ans, length)
    visited[cx][cy] = False  # 백트래킹 시 방문 상태 초기화
    return


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]

    # for c in mountain: print(c)

    chk_max = 0
    for chk in mountain:
        chk_max = max(chk_max, max(chk))

    ans = 0
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == chk_max:
                temp_mountain = [row[:] for row in mountain]
                visited = [[False] * n for _ in range(n)]
                dfs(temp_mountain, i, j, 1, 1)

    print(f'#{tc} {ans}')

    # if tc == 3:break

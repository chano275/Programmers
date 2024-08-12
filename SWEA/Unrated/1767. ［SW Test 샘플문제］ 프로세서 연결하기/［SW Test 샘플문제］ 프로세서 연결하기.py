"""
0, n-1 이면 연결됨. 해당 좌표의 i, j 튜플로 set 에 in  >  지나가도 될지 판단할때 in하면 컨티뉴로 
visited 도 true로 
1이 연결된 좌표에서 배열의 값이 0인 부분으로 쭉~ 가면서 visited 체크 

최대한 많은 코어  << 이 조건 만족하면 최소의 전선 길이 

"""


def dfs(_visited, _start_point, idx, _core, _line):
    # 하나 찍었거나 이번꺼의 방향 모두 갔는데 못찍는거다?
    # start_point 다음꺼로 넘기기

    _cx, _cy = _start_point[idx][0], _start_point[idx][1]

    if _start_point[idx][0] == -1:  # _cx == -1 / 다 돌았음
        ans_core.append(_core)
        ans_line.append(_line)
        return

    if _cx == 0 or _cx == n - 1 or _cy == 0 or _cy == n - 1:
        dfs(_visited, _start_point, idx + 1, _core + 1, _line)
        return

    for i in range(5):
        if i == 4:dfs(_visited, _start_point, idx + 1, _core, _line)

        flag = 0

        temp_visited = [row[:] for row in _visited]
        nx, ny = _cx, _cy
        temp_nx, temp_ny = nx, ny
        temp_line = _line

        if i == 0 or i == 2:  # 위아래 체크
            while nx != chk[i]:  # 끝 아니면 계속 가
                nx += dxy[i][0]
                ny += dxy[i][1]
                if exi[nx][ny] == 1 or _visited[nx][ny] == 1: # 나가야 하면 flag 찍고 나가
                    flag = 1
                    break

            if flag == 0:
                # 끝까지 갈 수 있다? 다시 돌면서 [ visited 찍고 / line 재서 + ]
                # 이 부분을 복사로 해서 넘기면 여러 분기로 갈라진 visited를 특별히 신경쓰지 않아도 됨
                while temp_nx != chk[i]:
                    temp_nx += dxy[i][0]
                    temp_ny += dxy[i][1]
                    temp_visited[temp_nx][temp_ny] = 1
                    temp_line += 1
                dfs(temp_visited, _start_point, idx + 1, _core + 1, temp_line)

        elif i==1 or i==3:  # 좌, 우 갈때 ( 아래 구성은 위와 동일 )
            while ny != chk[i]:
                nx += dxy[i][0]
                ny += dxy[i][1]
                if exi[nx][ny] == 1 or _visited[nx][ny] == 1:
                    flag = 1
                    break

            if flag == 0:
                while temp_ny != chk[i]:
                    temp_nx += dxy[i][0]
                    temp_ny += dxy[i][1]
                    temp_visited[temp_nx][temp_ny] = 1
                    temp_line += 1
                dfs(temp_visited, _start_point, idx + 1, _core + 1, temp_line)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 숫자 갯수
    exi = [list(map(int, input().split())) for _ in range(n)]
    visited = [row[:] for row in exi]

    start_point = []
    for i in range(n):
        for j in range(n):
            if exi[i][j] == 1:  # 왼오 위아래 쭉 dfs 찍으면 좋을거같은데
                start_point.append((i, j))
    start_point.append((-1, -1))

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (0,0)]
    chk = [n - 1, n - 1, 0, 0]
    core, line = 0, 0
    ans_core, ans_line = [], []
    dfs(exi, start_point, 0, core, line)

    check = max(ans_core)
    ans = float('inf')
    for i in range(len(ans_core)):
        if ans_core[i] == check:
            ans = min(ans, ans_line[i])

    print(f'#{tc} {ans}')

    # break
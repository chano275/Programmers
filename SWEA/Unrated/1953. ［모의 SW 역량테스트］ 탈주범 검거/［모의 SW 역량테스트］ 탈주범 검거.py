from collections import deque


tunnel_dict = {
    1:[(1,0), (0,1), (-1,0), (0,-1)],
    2:[(1,0), (-1,0)],
    3:[(0,1), (0,-1)],
    4:[(0,1), (-1,0)],
    5:[(1,0), (0,1)],
    6:[(1,0), (0,-1)],
    7:[(-1,0), (0,-1)]
}
T = int(input())
for tc in range(1, T+1):
    n,m,r,c,l = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    length = [[0] * m for _ in range(n)]
    # n * m 의 터널
    # 뚜껑의 좌표 r, c  /  소요시간 l
    queue = deque()
    queue.append((r,c))
    length[r][c] = 1
    while queue:
        cx, cy = queue.popleft()
        visited[cx][cy] = True

        for dxy in tunnel_dict[maps[cx][cy]]:  # 반
            dx, dy = dxy
            nx, ny = dx + cx, dy + cy

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if maps[nx][ny] == 0: continue
            if visited[nx][ny]: continue
            if (-dx, -dy) not in tunnel_dict[maps[nx][ny]]: continue

            length[nx][ny] = length[cx][cy] + 1
            queue.append((nx, ny))
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if 1<= length[i][j] <= l:
                ans += 1

    print(f'#{tc} {ans}')

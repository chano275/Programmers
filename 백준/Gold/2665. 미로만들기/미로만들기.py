from collections import deque

def bfs():
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0  # 시작 방은 항상 흰 방이므로 변환 필요 없음

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = dx + cx, dy + cy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 다음 방으로 이동하는 비용 계산
            if maps[nx][ny] == 0:  # 검은 방
                cost = visited[cx][cy] + 1
            else:  # 흰 방
                cost = visited[cx][cy]

            # 방문하지 않았거나 더 낮은 비용으로 방문 가능하면 업데이트
            if visited[nx][ny] == -1 or cost < visited[nx][ny]:
                visited[nx][ny] = cost
                queue.append((nx, ny))

    return visited[n-1][n-1]

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
print(bfs())

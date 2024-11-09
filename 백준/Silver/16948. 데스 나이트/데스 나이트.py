from collections import deque

def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)
    ans = 0

    while queue:
        temp_queue = deque()
        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) == (death[2], death[3]):
                return ans
            for dx, dy in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
                nx, ny = cx + dx, cy + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if v[nx][ny]:
                    continue

                temp_queue.append((nx, ny))
                v[nx][ny] = True
        queue = temp_queue
        ans += 1

    return -1

n = int(input())
death = list(map(int, input().split()))

visited = [[False] * n for _ in range(n)]
visited[death[0]][death[1]] = True
print(bfs((death[0], death[1]), visited))

from collections import deque


def bfs(start):
    global ans
    visited = [False] * 1000001

    queue = deque()
    queue.append(start)

    visited[start[0]] = True

    while queue:
        cx, depth = queue.popleft()

        if cx == g:
            ans = depth
            return

        for dx in [u, -d]:
            nx = cx + dx

            # 2개의 방향으로 보내야 함
            if nx < 1 or nx > f:continue
            if visited[nx]:continue
            queue.append((nx, depth + 1))
            visited[nx] = True

    return


f,s,g,u,d = list(map(int, input().split()))
ans = float('inf')
bfs((s, 0))
if ans == float('inf'): print('use the stairs')
else:print(ans)
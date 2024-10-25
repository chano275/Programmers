from collections import deque


def bfs(start_point):
    temp = 0
    queue = deque()
    queue.append(start_point)

    v_set = set()

    while queue:
        cx, cy = queue.popleft()
        visited[cx][cy] = True
        temp += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or ny < 0 or nx >= m or ny >= n:continue
            if visited[nx][ny]: continue
            if(nx, ny) in v_set:continue

            queue.append((nx, ny))
            v_set.add((nx, ny))


    return temp

m, n, k = list(map(int, input().split()))
squares = [list(map(int, input().split())) for _ in range(k)]  # m x n

ssang = set()
maps = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for s in squares:
    for p in range (s[1], s[3]):
        for q in range (s[0], s[2]):
            ssang.add((p, q))
            visited[p][q] = True
            maps[p][q] = 1

ans = []


for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and visited[i][j] == False:
            ans.append(bfs((i, j)))



ans = sorted(ans)

print(len(ans))

for i in range(len(ans)):
    print(ans[i], end = ' ')

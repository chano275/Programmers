from collections import deque

def bfs(v, start_point, i_num):
    queue = deque()
    queue.append(start_point)
    v[start_point[0]][start_point[1]] = True
    island_dict[i_num].append(start_point)
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not v[nx][ny]:
                v[nx][ny] = True
                queue.append((nx, ny))
                island_dict[i_num].append((nx, ny))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
island_dict = {}
island_number = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not visited[i][j]:
            island_dict[island_number] = []
            bfs(visited, (i, j), island_number)
            island_number += 1

edges = []
for key, val in island_dict.items():
    for (cx, cy) in val:
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx + dx, cy + dy
            dist = 0
            while 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    if dist >= 2:
                        for k, v in island_dict.items():
                            if (nx, ny) in v and k != key:
                                edges.append((dist, key, k))
                    break
                nx += dx
                ny += dy
                dist += 1

# Kruskal's algorithm
edges = sorted(edges)
parent = [i for i in range(island_number)]
result = 0
count = 0

for edge in edges:
    dist, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist
        count += 1
        if count == island_number - 1:
            break

if count == island_number - 1:
    print(result)
else:
    print(-1)

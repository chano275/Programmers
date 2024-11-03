from collections import deque

n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
s, x, y = list(map(int, input().split()))

start_dict = {}

visited = set()
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            visited.add((i, j))
            if maps[i][j] in start_dict:
                start_dict[maps[i][j]].append((i, j))
            else:
                start_dict[maps[i][j]] = [(i, j)]

while s != 0:
    s -= 1
    temp_dict = {}
    queue = deque()
    for k in sorted(start_dict.keys()):
        v = start_dict[k]
        if len(v) == 1:
            queue.append((k, v[0]))
            visited.add(v[0])
        else:
            for l in range(len(v)):
                queue.append((k, v[l]))
                visited.add(v[l])

    while queue:
        val, (cx, cy) = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in visited:
                continue
            if maps[nx][ny] != 0:
                continue  # 이미 바이러스가 있으면 넘어감

            maps[nx][ny] = val
            visited.add((nx, ny))
            if val in temp_dict:
                temp_dict[val].append((nx, ny))
            else:
                temp_dict[val] = [(nx, ny)]

    start_dict = temp_dict
    
print(maps[x-1][y-1])

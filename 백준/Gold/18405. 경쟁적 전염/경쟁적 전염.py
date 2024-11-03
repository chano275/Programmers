from collections import deque


n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
s, x, y = list(map(int, input().split()))  # s초 뒤 x, y에 존재하는 -1 -1 해주기

start_dict = {}

visited = set()
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:  # 시작 point 

            visited.add((i, j))  # 맨 처음에만 하면 좋을듯? 

            if maps[i][j] in start_dict:  # 키 이미 있으면
                start_dict[maps[i][j]].append((i, j))
            else:
                start_dict[maps[i][j]] = [(i, j)]

while s != 0:
    # for m in maps:print(m)
    # print('###############################')
    s -= 1

    temp_dict = {}   # visited 만들어놨음... k, v 돌면서 큐 채우고 

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

            if nx < 0 or nx >= n or ny < 0 or ny >= n:continue
            if (nx, ny) in visited:continue  # 이게 아래랑 사실 동일한거 아닌가? 
            if maps[nx][ny] != 0: continue

            maps[nx][ny] = val
            
            if maps[nx][ny] in temp_dict:  temp_dict[maps[nx][ny]].append((nx, ny))
            else:                          temp_dict[maps[nx][ny]] = [(nx, ny)]

            visited.add((nx, ny))

    start_dict = temp_dict
    
print(maps[x-1][y-1])
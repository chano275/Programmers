from  collections import deque


r, c = map(int, input().split())
maps = [list(map(str, input())) for _ in range(r)]

# D : 비버굴 / S : 고슴도치 / * : 물 / X : 돌 / . : 그냥
# S, *가 동시에 들어가면?


water = set()
water_sp = []

visited = set()

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            sp = [(i, j)]
            visited.add((i, j))

        elif maps[i][j] == '*':
            water.add((i, j))  # water 채우면서 map 보는게 아니라
            water_sp.append((i, j))
            visited.add((i, j))

queue = deque(sp)
water_queue = deque(water_sp)

ans = 0
ans_flag = 0

while 1:
    ans += 1
    temp = []
    temp_water = []

    while water_queue:  # 큐가 한번 빌떄까지? temp water_queue 에 다음꺼 저장해서 돌리기?
        cx_w, cy_w = water_queue.popleft()  #
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx_w, ny_w = cx_w + dx, cy_w + dy
            if nx_w < 0 or nx_w >= r or ny_w < 0 or ny_w >= c:continue
            if (nx_w, ny_w) in water or (nx_w, ny_w) in visited:continue
            if maps[nx_w][ny_w] == 'X' or maps[nx_w][ny_w] == 'D':continue  # 돌이면 못가

            water.add((nx_w, ny_w))
            temp_water.append((nx_w, ny_w))
            visited.add((nx_w, ny_w))

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:continue
            if (nx, ny) in water or (nx, ny) in visited:continue
            if maps[nx][ny] == 'X':continue

            if maps[nx][ny] == 'D':
                ans_flag = 1
                break

            temp.append((nx, ny))
            visited.add((nx, ny))

        if ans_flag == 1:break
    if ans_flag == 1:break

    water_queue = deque(temp_water)  # 한칸 보냈으니까 또 확인
    queue = deque(temp)

    if not queue:break


if ans_flag == 1:print(ans)
else:print('KAKTUS')
from collections import deque


def bfs(start_point):  # 현재 층 / x / y
    global ans
    queue = deque()
    queue.append(start_point)

    v = {start_point[0:3], }

    while queue:
        # print(queue)
        floor, cx, cy, depth = queue.popleft()

        if building[floor][cx][cy] == 'E':  # 탈출조건
            ans = depth
            return

        # 층 이동 없는 DFS
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:  # 한층 내에서 4방향 탐색은 이 for문으로
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if (floor, nx, ny) in v: continue
            if building[floor][nx][ny] == '#':continue

            queue.append((floor, nx, ny, depth + 1))
            v.add((floor, nx, ny))

        # 층 이동 있는 DFS
        if 0 <= floor + 1 <= l - 1:  # 0 ~ l-1
            if building[floor + 1][cx][cy] != '#' and (floor + 1, cx, cy) not in v:  # 갈수 있고 방문 안했으면
                queue.append((floor + 1, cx, cy, depth + 1))
                v.add((floor + 1, cx, cy))

        if 0 <= floor - 1 <= l - 1:  # 0 ~ l-1
            if building[floor - 1][cx][cy] != '#' and (floor - 1, cx, cy) not in v:  # 갈수 있고 방문 안했으면
                queue.append((floor - 1, cx, cy, depth + 1))
                v.add((floor - 1, cx, cy))

    return


def find_S():
    for q in range(l):
        for w in range(r):
            for e in range(c):
                if building[q][w][e] == 'S':
                    return q, w, e, 0

while 1:
    # l : 층수  /  r c : 행 열
    l, r, c = list(map(int, input().split()))
    if (l, r, c) == (0, 0, 0): break

    building = []

    for _ in range(l):
        maps = [list(map(str, input())) for _ in range(r)]
        blank = input()
        building.append(maps)

    # for b in building:print(b)

    ans = float('inf')
    bfs(find_S())

    if ans == float('inf'):print('Trapped!')
    else: print(f'Escaped in {ans} minute(s).')
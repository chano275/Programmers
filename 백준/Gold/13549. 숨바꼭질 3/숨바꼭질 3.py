from collections import deque

def bfs():
    queue = deque()
    queue.append((n, 0))  # 현재 위치와 시간

    visited = [-1] * 100001
    visited[n] = 0

    while queue:
        cx, time = queue.popleft()

        if cx == k:
            return time

        for dx in [1, -1, cx]:
            if dx == cx:
                nx = cx * 2  # 순간이동
                new_time = time  # 시간 증가 없음
            else:
                nx = cx + dx
                new_time = time + 1  # 시간 1 증가

            if 0 <= nx <= 100000:
                if visited[nx] == -1 or visited[nx] > new_time:
                    visited[nx] = new_time
                    if dx == cx:
                        queue.appendleft((nx, new_time))  # 시간이 소요되지 않는 이동
                    else:
                        queue.append((nx, new_time))  # 일반 이동

    return -1

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    print(bfs())

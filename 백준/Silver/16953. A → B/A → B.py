from collections import deque


def bfs(start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    ans = 0
    while 1:

        if not queue:return -1

        temp_queue = deque()
        ans += 1

        while queue:
            cx = queue.popleft()
            for dx in [cx, 9*cx + 1]:
                nx = cx+dx
                if nx in visited:continue
                if nx >= 10 ** 9 + 1:continue

                if nx == b:return ans + 1

                temp_queue.append(nx)
                visited.add(nx)

        queue = temp_queue


a, b = map(int, input().split())
print(bfs(a))
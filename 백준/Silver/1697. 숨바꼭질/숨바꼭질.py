from collections import deque


def bfs():  # x-1 x+1 2*x
    queue = deque()
    queue.append(n)  # 수빈이 위치 n
    ans = 0

    visited = [False] * 100001
    visited[n] = True  # -1 ?

    while 1:
        # print(queue)
        ans += 1
        # if not queue: return ans

        temp_queue = deque()

        while queue:
            cx = queue.popleft()
            for dx in [1, -1, cx]:  #
                nx = cx + dx

                if nx < 0 or nx > 100000:continue
                if visited[nx]:continue

                visited[nx] = True
                temp_queue.append(nx)

                if nx == k: return ans

        queue = temp_queue

    return


n, k = map(int, input().split())
if n == k:print(0)
else:
    print(bfs())


t = 10
for tc in range(1, t+1):
    v, e = map(int, input().split())
    ori_edge = list(map(int, input().split()))

    zin_ip = [0] * (v+1)
    graph = [[] for _ in range(v+1)]

    for i in range(e):
        front = ori_edge[2 * i]
        rear  = ori_edge[2 * i + 1]

        zin_ip[rear] += 1
        graph[front].append(rear)

    from collections import deque


    visited = []
    queue = deque()
    for i in range(1, len(zin_ip)):
        if zin_ip[i] == 0:
            visited.append(i)
            queue.append(i)

    while queue:
        cur = queue.popleft()

        for elem in graph[cur]:
            zin_ip[elem] -= 1

        for i in range(1, len(zin_ip)):
            if zin_ip[i] == 0 and i not in visited:
                queue.append(i)
                visited.append(i)

    print(f'#{tc} ', end = '')
    for elem in visited:
        print(elem, end = ' ')

    print('')
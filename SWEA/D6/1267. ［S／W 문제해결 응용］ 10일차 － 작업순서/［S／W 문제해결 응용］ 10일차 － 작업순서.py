from collections import deque


def wisang():
    visited = []
    queue = deque()
    for i in range(1, len(zin_ip)):
        if zin_ip[i] == 0:
            queue.append(i)
            visited.append(i)

    while queue:
        cur = queue.popleft()
        for elem in graph[cur]:
            zin_ip[elem] -= 1

        for i in range(1, len(zin_ip)):
            if zin_ip[i] == 0 and i not in visited:
                queue.append(i)
                visited.append(i)

    return visited




t = 10
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    original_edge = list(map(int, input().split()))

    zin_ip = [0] * (v+1)
    graph = [[0] * (v+1) for _ in range(v+1)]

    for i in range(e):  # original_edge[2*i] > original_edge[2*i + 1]
        zin_ip[original_edge[2*i + 1]] += 1
        graph[original_edge[2*i]].append(original_edge[2*i + 1])

    print(f'#{tc} ', end = '')
    for elem in wisang():
        print(elem, end = ' ')
    print('')



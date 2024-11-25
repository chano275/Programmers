from collections import deque


def wisang():
    ans = []
    queue = deque()

    ## 맨 처음
    for i in range(1, len(zinip)):  # 1부터 v까지
        if zinip[i] == 0:
            queue.append(i)
            vertex_set.discard(i)


    while queue:
        cur = queue.popleft()
        ans.append(cur)

        for element in graph[cur]:  zinip[element] -= 1

        for i in range(1, len(zinip)):  # 1부터 v까지
            if zinip[i] == 0 and i in vertex_set:  #
                queue.append(i)
                vertex_set.discard(i)

    return ans



t = 10
for tc in range(1, t+1):
    v, e = map(int, input().split())
    edge_list = list(map(int, input().split()))

    zinip = [0] * (v + 1)               # 0 idx 안쓸것
    vertex_set = set()
    for i in range(1, v+1):vertex_set.add(i)


    graph = [[] for _ in range(v + 1)]  # 0행 안쓸 것
    for i in range(e):
        left, right = edge_list[2 * i], edge_list[2 * i + 1]
        graph[left].append(right)
        zinip[right] += 1

    ret = wisang()

    print(f'#{tc}', end = ' ')
    for elem in ret:
        print(elem, end = ' ')
    print('')
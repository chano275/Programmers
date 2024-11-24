from collections import deque


def wisang():
    visited = []
    queue = deque()
    for i in range(1, len_v + 1):
        if zinip[i] == 0:  # 진입차수 없는 원소
            queue.append(i)
            # visited.append()  # popleft에서 해줄까... 
    
    while queue:
        cur = queue.popleft()
        visited.append(cur)
        for elem in graph[cur]:
            zinip[elem] -= 1

        for i in range(1, len_v + 1):
            if zinip[i] == 0 and i not in visited and i not in queue:  # 이게 되나 
                queue.append(i)

    return visited


t = 10
for tc in range(1, t+1):
    len_v, len_e = map(int,input().split())
    edges = list(map(int, input().split()))


    zinip = [0] * (len_v + 1)               # 진입차수 배열의 첫 원소 무시해야 
    graph = [[] for _ in range(len_v + 1)]  # 그래프의 첫줄 무시해야 

    for i in range(len_e):
        graph[edges[2 * i]].append(edges[2 * i + 1])  # 왼쪽 정점에서 오른쪽 정점으로 향하는 그래프 > 연결되는 
        zinip[edges[2 * i + 1]] += 1

    # for line in graph:
    #     print(line)
    # print(zinip)

    ans = wisang()

    print(f'#{tc} ', end = '')
    for a in ans:
        print(a, end = ' ')
    print('')
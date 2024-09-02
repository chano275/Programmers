from collections import deque


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(m)]
    maps = [[0] * n for _ in range(n)]

    for l in li:
        if len(l) == 1:  # 나중에 생각해줘야 함
            pass
        else:
            maps[l[0]-1][l[1]-1] = 1
            maps[l[1]-1][l[0]-1] = 1


    visited = [False] * n
    ans = 0
    for i in range(n):
        if visited[i] == False:
            queue = deque()
            queue.append(i)
            ans += 1
            while queue:
                now = queue.popleft()
                visited[now] = True
                for j in range(n):
                    if maps[now][j] != 0:  # 이어져 있다.
                        if visited[j] == True: continue
                        visited[j] = True
                        queue.append(j)

    print(f'#{tc} {ans}')
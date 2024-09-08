from itertools import combinations
from collections import deque

def is_connected(area, will_visit):
    visited = set([area[0]])
    queue = deque([area[0]])

    while queue:
        cur = queue.popleft()
        for neighbor in maps[cur]:
            if neighbor in will_visit and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited == set(will_visit)

n = int(input())
population = list(map(int, input().split()))
li = [list(map(int, input().split())) for _ in range(n)]
numbers = [q for q in range(1, n+1)]

if n == 2:
    print(abs(population[0] - population[1]))
else:
    maps = {}
    for idx, l in enumerate(li, start=1):
        maps[idx] = l[1:]

    compare = []
    for i in range(1, n//2 + 1):
        target = list(combinations(numbers, i))
        for t in target:
            oppo_target = tuple(set(numbers) - set(t))
            compare.append([t, oppo_target])

    ans = float('inf')
    chk_set = set()

    for com in compare:
        area_l, area_r = com[0], com[1]
        if len(area_l) == len(area_r) and area_l in chk_set:
            continue
        chk_set.add(area_r)

        # 왼쪽과 오른쪽 구역이 각각 연결되었는지 확인
        if is_connected(area_l, area_l) and is_connected(area_r, area_r):
            ans_l = sum(population[i-1] for i in area_l)
            ans_r = sum(population[i-1] for i in area_r)
            ans = min(ans, abs(ans_l - ans_r))

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

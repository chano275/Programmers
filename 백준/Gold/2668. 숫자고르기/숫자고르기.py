def dfs(start, cur, _visited):
    global ans

    visited_first[cur] = True
    _visited.append(cur)  # #####3

    if next[cur] in _visited:
        idx = _visited.index(next[cur])  # #####3
        cycle_nodes = _visited[idx:]     # #####3
        ans.update(cycle_nodes)          # #####3
        return

    if not visited_first[next[cur]]:
        dfs(start, next[cur], _visited)

    _visited.pop()  # #####3

    return

n = int(input())
first = [i for i in range(n + 1)]  # 0 ~ n
next = [int(input()) for _ in range(n)]  # 1 ~ n번째 idx에 들어있는 원소
next = [-1] + next
visited_first = [False] * (n+1)
ans = set()  # #####3

for i in range(1, n+1):
    if not visited_first[i]:
        visited = []
        dfs(i, i, visited)

print(len(ans))  # #####3
for i in sorted(ans):  # #####3
    print(i)

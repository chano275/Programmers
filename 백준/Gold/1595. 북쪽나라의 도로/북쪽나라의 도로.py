import sys


def dfs(cur, depth, visited):
    global ans

    for v in graph[cur]:
        if v[0] in visited:
            continue
        visited.add(v[0])

        dfs(v[0], depth + v[1], visited)
        # visited.discard(v[0])  # 왜 빼야하지 ?

    ans = max(ans, depth)
    return

# 2개의 도시, 연결 도로 길이 / 양방향 통행 가능
# 거리가 가장 먼 두 도시 사이의 거리를 출력하는 것이 당신의 임무
# 도시1  /  도시2  /  edge 길이
edges = []

while True:
    try:
        line = input().strip()
        if not line:
            continue  # 빈 줄은 무시하고 다음 입력을 받습니다.
        edges.append(list(map(int, line.split())))

    except EOFError:
        break  # EOFError가 발생하면 입력이 끝났으므로 루프를 종료합니다.

if not edges:
    print(0)
else:

    graph = {}
    for edge in edges:
        a, b, w = edge
        if a in graph:
            graph[a].append((b, w))
        else:
            graph[a] = [(b, w)]

        if b in graph:
            graph[b].append((a, w))
        else:
            graph[b] = [(a, w)]

    ans = 0
    for node in graph:
        dfs(node, 0, {node})  # cur, depth, visited

    print(ans)
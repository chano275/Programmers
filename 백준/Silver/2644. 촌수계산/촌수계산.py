"""
dfs 적으로 생각...
k가 아닐 때까지 올리기 / v 있으면 v에 모두 보내기 / depth 하나씩 올리면서 해당 값이 b면 depth return
"""
import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)

# visited 써야하네 ;


def dfs(current, depth, visited):
    # print(current, depth)
    global ans
    if current == b:
        ans = min(ans, depth)
        return

    # 부모 check
    for k, v in family_dict.items():
        if current in v:  # 부모가 있다 / 부모는 여러명이 아니다
            if k not in visited:
                dfs(k, depth + 1, visited + [current])
            break

    # 자식 check
    if current in family_dict:  # 자식이 있다
        for v in family_dict[current]:
            if v not in visited:
                dfs(v, depth + 1, visited + [current])
    else:  # 자식이 없다 / b 아니었으니까 여기 왔잖아?
        return

    # 부모로 소식 보냈거나 / 최상위노드 -> 위아래로 / 아래로 소식 이미 보냈으므로
    return


n = int(input())  # 사람 수
a, b = map(int, input().split())  # 촌수 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식간의 관계의 개수


xy = [list(map(int, input().split())) for _ in range(m)]  # 부모 < 자식
family_dict = {}
for fam in xy:  # 유사트리
    if fam[0] not in family_dict:
        family_dict[fam[0]] = [fam[1]]
    else:family_dict[fam[0]].append(fam[1])
# print(family_dict)


ans = float('inf')
dfs(a, 0, [])  # 방문 부모 / sibilings 넣을 visited 배열

if ans == float('inf'):print(-1)
else: print(ans)
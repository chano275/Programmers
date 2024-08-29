def dfs(who, depth, _set):
    if depth == 2:
        _set.add(who)
        two_friends[start_point] += 1
        return

    if who not in friends_dict: return
    for v in friends_dict[who]:
        _set.add(v)
        dfs(v, depth + 1, _set)
        # _set.discard()


n = int(input())
friends = [list(map(str, input())) for _ in range(n)]
two_friends = [0] * n

friends_dict = {}
for i in range(n):
    for j in range(n):
        if friends[i][j] == 'Y':
            if i not in friends_dict:
                friends_dict[i] = [j]
            else: friends_dict[i].append(j)

# print(friends_dict)


for i in range(n):
    temp_set = set()
    start_point = i
    dfs(i, 0, temp_set) # 연결되어 있는 k들의 v들

    if not temp_set:
        two_friends[i] = 0
        continue

    temp_set.remove(i)
    two_friends[i] = len(temp_set)

print(max(two_friends))


"""
가장 유명한 사람을 구하는 방법 > 각 사람의 2-친구를 구하면 된다. 

A B의 2-친구가 되기 위해서 : 두 사람이 친구 / A와 or B와 친구인 C가 존재

여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 
가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.


입력
첫째 줄에 사람의 수 N이 주어진다. 
N은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

출력
첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.
"""
import itertools


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(1, n+1)]
# n 짝수 /  n//2로 팀 나눔
# i, j가 같은 팀에 속했을 때에 팀의 능력치에 +되는 수 : maps


# 반반 조합 -> 2개씩 순열

li = (list(itertools.combinations(people, n//2)))
rev_li = []
for l in li:
    temp = []
    for i in range(len(people)):
        if people[i] in l:pass
        else:temp.append(people[i])
    rev_li.append(tuple(temp))

# print(li)
# print(rev_li)

sum_min = float('inf')

for i in range(len(li)):
    sum_l, sum_r = 0,0

    li_p = list(itertools.permutations(li[i], 2))
    rev_p = list(itertools.permutations(rev_li[i], 2))
     
    # print(li_p)
    # print(rev_p)

    for j in range(len(li_p)):
        sum_l += maps[li_p[j][0]-1][li_p[j][1]-1]
        sum_r += maps[rev_p[j][0]-1][rev_p[j][1]-1]

    sum_min = min(sum_min, abs(sum_r - sum_l))

print(sum_min)






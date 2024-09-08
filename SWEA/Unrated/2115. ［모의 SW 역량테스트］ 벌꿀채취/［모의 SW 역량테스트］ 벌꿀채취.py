from itertools import combinations


T = int(input())
for tc in range(1, T+1):
    n, m, c = list(map(int, input().split()))

    maps = [list(map(int, input().split())) for _ in range(n)]
    numbers = [q for q in range(n)]



    bees = []
    for i in range(n):
        for j in range(n-m + 1):  # 3 > 012 
            temp = maps[i][j:j+m]
            # c에 가장 가까운 max와 (i, j+m) 저장
            
            ms_temp = 0
            for w in range(1, len(temp) + 1):
                comb_temp = list(combinations(temp, w))
                for chk in comb_temp:
                    if sum(chk) <= c:
                        te_temp = 0
                        for te in chk:
                            te_temp += te ** 2
                        ms_temp = max(ms_temp, te_temp)
            bees.append((ms_temp, (i, j, j+m-1)))

    bees_pick = list(combinations(bees, 2))

    ans = 0
    for b in bees_pick:
        if b[0][1][0] != b[1][1][0] or b[0][1][2] < b[1][1][1]:
            ans = max(ans, b[0][0] + b[1][0])

    print(f'#{tc} {ans}')

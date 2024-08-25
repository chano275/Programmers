dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 하 우 상 좌
T = int(input())
for tc in range(1, T+1):
    n, m, k = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(n)]

    first = {}

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0:
                # 상태 : 비활 / 활 / 죽 : 0 / 1 / -1
                first[(i, j)] = [ maps[i][j], maps[i][j], 0] # 에너지 / 상태 전환까지 남은 시간 / 상태

    for i in range(k):
        temp = {}

        for elem_key, elem_val in first.items():

            if elem_val[2] == 0: # 비활성화
                if elem_val[1] == 1: temp[elem_key] = [elem_val[0], elem_val[0], 1]  # 이번 시간에 변해야해 > 활성화
                else: temp[elem_key] = [elem_val[0], elem_val[1] - 1, 0]  # 안변해도 됨 : 단순히 시간 보내기

            elif elem_val[2] == 1:  # 활성화
                if elem_val[0] == elem_val[1]:  # 활성화된 줄기 세포의 첫 한시간 : 4방향으로 복제
                    cx, cy = elem_key
                    for dx, dy in dxy:
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) in first:continue  # 원소가 있었던 자리 -> 못들어가
                        else:
                            if (nx, ny) in temp:  # 동일하게 뻗는거 : 비교해서 생존력 더 큰거 살리기
                                if temp[(nx, ny)][0] >= elem_val[0]: continue
                                else: temp[(nx, ny)] = [elem_val[0], elem_val[0], 0]
                            else: temp[(nx, ny)] = [elem_val[0], elem_val[0], 0]

                    if elem_val[1] == 1:temp[elem_key] = [elem_val[0], elem_val[1] - 1, -1]  # 1,1이면 뻗고 바로 죽어야
                    else: temp[elem_key] = [elem_val[0], elem_val[1] - 1, 1]                 # 1 아니면 뻗고 줄이기

                elif elem_val[1] == 1: temp[elem_key] = [elem_val[0], elem_val[1] - 1, -1]  # 죽어야 할 때..
                else:temp[elem_key] = [elem_val[0], elem_val[1] - 1, 1]

            else:  # 비활성화 상태
                temp[elem_key] = elem_val

        first = temp

    ans = 0
    for chk in first.values():
        if chk[2] == 0 or chk[2] == 1: ans += 1
    print(f'#{tc} {ans}')
    # break
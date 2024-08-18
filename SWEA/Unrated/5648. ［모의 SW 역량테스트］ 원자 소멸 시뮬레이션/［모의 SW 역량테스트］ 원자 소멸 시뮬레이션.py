# 0 상 / 1 하 / 2 좌 / 3 우
dxy = [(0,0.5), (0,-0.5), (-0.5,0), (0.5,0)]
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    atoms_list = [list(map(int, input().split())) for _ in range(n)]
    # x y dir k

    ans = 0

    first_dict = {}
    for single in atoms_list:
        first_dict[(single[0], single[1])] = [(single[2], single[3])]

    while first_dict:  # 다 비면 out
        temp_dict = {}
        for k, v in first_dict.items():
            cx, cy = k
            dx, dy = dxy[v[0][0]]
            nx, ny = cx + dx, cy + dy

            if nx < -1000 or ny < -1000 or nx > 1000 or ny >= 1000: continue
            # 범위 밖으로 안나가면 ok
            if (nx, ny) in temp_dict:
                temp_dict[(nx, ny)].append(v[0]) # v[0]이 이미 튜플이야
            else:
                temp_dict[(nx, ny)] = v

        first_dict = {}
        # temp dict에 이동시킨 거 넣었음. 만나는거 체크
        for k, v in temp_dict.items():
            if len(v) > 1:
                for chk in v:
                    ans += chk[1]
            else:
                first_dict[k] = v

    print(f'#{tc} {ans}')

#     break
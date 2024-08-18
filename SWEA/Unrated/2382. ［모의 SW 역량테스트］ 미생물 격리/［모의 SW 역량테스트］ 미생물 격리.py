

dxy = [(1,0), (0,1), (-1,0), (0,-1)]
T = int(input())
for tc in range(1, T+1):
    n, m, k = list(map(int, input().split()))
    micros_list = [list(map(int, input().split())) for _ in range(k)]

    first_dict = {}
    # (x, y) = [ (수, 방향) , ...]
    for temp in micros_list:
        first_dict[(temp[0], temp[1])] = [(temp[2], temp[3])]

    for _ in range(m):
        second_dict = {}
        for k, v in first_dict.items():
            cx, cy = k
            if v[0][1] == 1: dx, dy = dxy[2]
            elif v[0][1] == 2: dx, dy = dxy[0]
            elif v[0][1] == 3: dx, dy = dxy[3]
            elif v[0][1] == 4: dx, dy = dxy[1]
            nx, ny = cx + dx, cy + dy

            # if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:  # 벽 부딫힘
                # 겹치는거 생각 안해도 괜찮음
                if v[0][1] == 1:second_dict[(nx, ny)] = [(v[0][0] // 2, 2)]
                elif v[0][1] == 2:second_dict[(nx, ny)] = [(v[0][0] // 2, 1)]
                elif v[0][1] == 3:second_dict[(nx, ny)] = [(v[0][0] // 2, 4)]
                elif v[0][1] == 4:second_dict[(nx, ny)] = [(v[0][0] // 2, 3)]
            else:
                # 벽 안부딫힘 :
                if (nx, ny) in second_dict:
                    second_dict[(nx, ny)].append((v[0][0], v[0][1]))
                else:
                    second_dict[(nx, ny)] = v

        first_dict = {}


        for k, v in second_dict.items():
            if len(v) > 1:
                _max, _sum, _dir = 0, 0, 0
                for chk in v:
                    _sum += chk[0]

                    temp = _max
                    _max = max(_max, chk[0])
                    if temp != _max:
                        _dir = chk[1]

                first_dict[k] = [(_sum, _dir)]

            else:
                first_dict[k] = v

    ans = 0
    for k, v in first_dict.items():
        ans += v[0][0]

    print(f'#{tc} {ans}')

    # break
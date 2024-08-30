def checker(line):
    cnt = 1

    for i in range(1, len(line)):

        if line[i] - line[i-1] == 0:
            cnt += 1
            if cnt >= l:cnt = l

        elif line[i] - line[i-1] == 1:  # 올라옴
            if cnt == l: cnt = 1
            else:return 0

        elif line[i] - line[i - 1] == -1:  # 내려옴
            if cnt < 0: return 0
            cnt = -l + 1

        else:return 0

    if cnt >= 0: return 1
    return 0


n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
maps_temp = list(map(list, zip(*maps)))

ans = 0

for m in maps:
#    temp_ans = ans
    ans += checker(m)
#    if ans != temp_ans:print(m)
for m_t in maps_temp:
#    temp_ans = ans
    ans += checker(m_t)
#    if ans != temp_ans:print(m_t)

print(ans)
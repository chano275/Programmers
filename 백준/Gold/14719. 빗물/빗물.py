h, w = map(int, input().split())
maps = list(map(int, input().split()))

ans = 0

# 왼쪽에서부터의 최대 높이를 기록
left_max = [0] * w
left_max[0] = maps[0]

for i in range(1, w):
    left_max[i] = max(left_max[i - 1], maps[i])

# 오른쪽에서부터의 최대 높이를 기록
right_max = [0] * w
right_max[-1] = maps[-1]

for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], maps[i])

# 각 블록에서 물이 고일 수 있는 높이를 계산
for i in range(w):
    ans += min(left_max[i], right_max[i]) - maps[i]

print(ans)

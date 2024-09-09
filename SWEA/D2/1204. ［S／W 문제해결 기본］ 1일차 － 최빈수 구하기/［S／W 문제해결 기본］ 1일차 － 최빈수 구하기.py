from collections import deque
tc = int(input())

for _ in range(1, tc+1):
    test_case = int(input())
    score = list(map(int, input().split()))
    cnt = [0] * (max(score) + 1)

    for i in range(len(score)):cnt[score[i]] += 1

    maxv = 0
    max_cnt = max(cnt)
    for j in range(len(cnt)):
        if max_cnt == cnt[j]:
            maxv = max(maxv, j)

    print(f"#{test_case} {maxv}")
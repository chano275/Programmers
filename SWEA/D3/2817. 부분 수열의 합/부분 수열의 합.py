def dfs(idx, sum_k):
    global answer
    if sum_k == K:
        answer += 1
        return
    if sum_k > K:
        return
    if idx == N:
        return
    dfs(idx + 1, sum_k + A[idx])
    dfs(idx + 1, sum_k)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0
    dfs(0, 0)
    print(f'#{tc} {answer}')
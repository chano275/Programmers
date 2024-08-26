
import heapq
r, c, k = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(3)]
ans = -1
a = [p[:] for p in maps]
num_dict = {}
time = 0

# a의 idx 1부터 시작한다고 해서 r, c -1씩?
for _ in range(101):
    if r-1 > len(a)-1 or c-1 > len(a[0])-1:pass
    else:
        if a[r-1][c-1] == k:        # 연산 끝나고 탈출조건 check
            ans = time
            break
    time += 1

    g, s, max_length = len(a[0]), len(a), 0  # 열 행

    temp = []
    if s >= g:  # 가로 그대로 가도 괜찮음.
        for line in a:  # line[i] 의 갯수를 세서,
            heap_temp, heap = [], []
            b = [0] * (max(line) + 1)  # 0번 idx 사용하지 않음
            for num in line:  b[num] += 1  # idx + 1
            for i in range(1, len(b)):
                if b[i] == 0: continue
                heapq.heappush(heap, (b[i], i))  # 횟수, 숫자
            while heap:
                a = (heapq.heappop(heap))  #
                heap_temp.append(a[1])
                heap_temp.append(a[0])
            temp.append(heap_temp)
            max_length = max(max_length, len(heap_temp))

        a = []
        for zero_padding in temp:
            if len(zero_padding) != max_length:  # 그만큼을 0 붙여줘야
                for _ in range(abs(len(zero_padding) - max_length)):
                    zero_padding.append(0)
            a.append(zero_padding)

    else:  # C연산
        # 돌리기
        s, g = len(a), len(a[0])
        temp = [[0] * s for _ in range(g)]
        for i in range(s):
            for j in range(g):
                temp[j][i] = a[i][j]
        a = temp

        temp = []
        # 위와 동일한 정렬 연산
        for line in a:  # line[i] 의 갯수를 세서,
            heap_temp, heap = [], []
            b = [0] * (max(line) + 1)
            for num in line:  b[num] += 1  # idx + 1
            for i in range(1, len(b)):  # 0번 idx 사용하지 않음
                if b[i] == 0: continue
                heapq.heappush(heap, (b[i], i))  # 횟수, 숫자

            while heap:
                a = (heapq.heappop(heap))  #
                heap_temp.append(a[1])
                heap_temp.append(a[0])
            temp.append(heap_temp)
            max_length = max(max_length, len(heap_temp))

        # 0 붙이기
        a = []
        for zero_padding in temp:
            if len(zero_padding) != max_length:  # 그만큼을 0 붙여줘야
                for _ in range(abs(len(zero_padding) - max_length)):
                    zero_padding.append(0)
            a.append(zero_padding)

        # 다시 돌리기
        s, g = len(a), len(a[0])
        temp = [[0] * s for _ in range(g)]
        for i in range(s):
            for j in range(g):
                temp[j][i] = a[i][j]
        a = temp

    s, g = len(a), len(a[0])
    temp = []
    if s > 100 and g > 100:
        for i in range(100):
            for j in range(100):
                temp[i][j] = a[i][j]
                a = temp
    elif s > 100:
        for i in range(100):
            for j in range(g):
                temp[i][j] = a[i][j]
                a = temp
    elif g > 100:
        for i in range(s):
            for j in range(100):
                temp[i][j] = a[i][j]
                a = temp

print(f'{ans}')
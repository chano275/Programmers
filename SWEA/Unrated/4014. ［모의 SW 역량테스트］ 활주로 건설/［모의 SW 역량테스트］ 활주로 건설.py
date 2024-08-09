T = int(input())
for tc in range(1, T+1):
    n, x = map(int, input().split())
    flight = [list(map(int, input().split())) for _ in range(n)]

    def checker(line):
        cnt, chk = 1, -1

        if len(line) < x : return 0

        for i in range(1, len(line)):

            if line[i] == line[i - 1]:
                cnt += 1

            elif line[i] == line[i - 1] + 1:
                if cnt >= x:
                      cnt = 1
                else: 
                    return 0

            elif line[i] == line[i - 1] - 1:
                if cnt < 0: 
                    return 0
                else:
                    cnt = -x + 1

            else: 
                return 0 # 차이 2 +- 이상 > 틀림

        if cnt >= 0:
            return 1
        else:
            return 0



    ans = 0

    for i in range(n): 
        ans += checker(flight[i])
        ans += checker([q[i] for q in flight])
        # print('###############################')
        # print(flight[i])
        # print(checker(flight[i]))
        # print('###############################')
        # print([q[i] for q in flight])
        # print(checker([q[i] for q in flight]))
        # print('###############################')
        
    print(f'#{tc} {ans}')

    #break

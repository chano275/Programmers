## Working on BOJ



def m():
    number = int(input())

    sung = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 0~9까지 성냥 개수
    cnt = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            if (4 + sung[i] + sung[j] + sung[k] + sung[l] + sung[m] + sung[n]) == number:
                                if (i * 10 + j) + (k * 10 + l) == (m * 10 + n):
                                    print(str(i)+str(j)+'+'+str(k)+str(l)+'='+str(m)+str(n))
                                    cnt = 1
                                    return

                                else:pass

    if cnt == 0:print('impossible')
    else:pass
    return

m()



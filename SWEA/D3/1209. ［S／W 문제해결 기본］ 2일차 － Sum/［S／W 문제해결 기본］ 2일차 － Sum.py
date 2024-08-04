for _ in range(1,11):
    test_case = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]

#    print(a)

    sum_a = [0] * 202

    for j in range(100):
        for i in range(100):
            sum_a[j] += a[j][i] #
            sum_a[j+100] += a[i][j]

            if i == j: sum_a[200]+= a[j][i]
            if i + j == 99: sum_a[201]+= a[j][i]


    print(f"#{test_case} {max(sum_a)}")
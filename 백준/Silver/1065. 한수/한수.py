def ones_():
    a = int(input())
    cnt = 0
    flag = 0
    for i in range (a):
        #i+1 이 봐야 하는 숫자
        check = str(i+1)
        if len(check)==1 or len(check) == 2:
            cnt = cnt+1
        else:
            test = int(check[0]) - int(check[1])
            for j in range (len(check)-1):
                test_ = int(check[j]) - int(check[j+1])
                if test_ != test:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                cnt = cnt+1
    print(cnt)   
ones_()

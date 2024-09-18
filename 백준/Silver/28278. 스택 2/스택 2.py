import sys

n = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(n):


    order = (sys.stdin.readline().rstrip())

    if len(order) == 1:a = int(order)
    else: a,b = map(int, order.split())

    #print('')
    #print(f"{stack} / {(a)} / {len(stack)}")
    if a==1: stack.append(b)
    elif a==2:
        if len(stack) != 0:
            print(stack[len(stack) - 1])
            stack.pop()
            #print(stack)
        else:print(-1)
    elif a==3:print(len(stack))
    elif a==4:
        if len(stack) == 0: print(1)
        else:print(0)
    else:
        if len(stack) != 0:print(stack[len(stack)-1])
        else:print(-1)

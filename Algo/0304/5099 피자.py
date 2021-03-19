for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ci = list(map(int, input().split()))

    num = [i for i in range(m)] # 인덱스 활용을 위해
    queue = num[0:n] # n개 까지 들어가니까

    while len(queue) != 1:
        if ci[queue[0]] != 1:
            ci[queue[0]] = ci[queue[0]]//2 # 한방 구우면 절반되니 나누고
            queue.append(queue.pop(0)) # 한방 구운거 다시 돌려주고
        else:
            queue.pop(0)
            if n != m: # m이랑 같아야 다 돌린거니까
                queue.append(num[n])
                n += 1
    print('#{} {}'.format(tc, queue[0]+1))
for tc in range(1, int(input())+1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]

    road = [0 for i in range(201)]

    for i in mapp:
        if i[0] < i[1]:
            move = (i[0]+1)//2
            stop = (i[1]+1)//2
        else:
            move = (i[1]+1)//2
            stop = (i[0]+1)//2
        for l in range(move, stop+1):
            road[l] += 1
    result = 0
    for i in road:
        if i > result:
            result = i
    print('#{} {}'.format(tc, result))
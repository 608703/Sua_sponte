def detect(p, t):
    s = 1
    e = p
    c = (s+e)//2
    cnt = 0
    while c != t:
        if t > c:
            s = c
        else:
            e = c
        cnt += 1
        c = (s+e)//2

    return cnt

for tc in range(1, int(input())+1):
    p, a, b = map(int, input().split())

    aa = detect(p, a)
    bb = detect(p, b)

    if aa > bb:
        print('#{} {}'.format(tc, 'B'))
    elif aa == bb:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 'A'))
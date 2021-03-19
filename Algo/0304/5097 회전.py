for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    trash = list(map(int, input().split()))

    for i in range(m):
        num = trash.pop(0)
        trash.append(num)

    print('#{} {}'.format(tc, trash[0]))
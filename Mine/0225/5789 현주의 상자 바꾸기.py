for tc in range(1, int(input())+1):
    n, q = map(int, input().split())

    list1 = ['0'] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            list1[j] = str(i)

    print('#{}'.format(tc), ' '.join(list1))
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    result = 0

    if n > m:
        for i in range(n-m+1):
            hop = 0
            for j in range(m):
                hop += list1[i+j] * list2[j]
            if hop > result:
                result = hop

    else:
        for i in range(m-n+1):
            hop = 0
            for j in range(n):
                hop += list2[i+j] * list1[j]
            if hop > result:
                result = hop

    print('#{} {}'.format(tc, result))
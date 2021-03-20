for tc in range(1, int(input())+1):
    n = int(input())
    list1 = list(map(int, input().split()))

    list1.sort()
    list2 = list1[::-1]
    result = []
    for i in range(5):
        result.append(list2[i])
        result.append(list1[i])

    print('#{}'.format(tc), end = ' ')
    for i in result:
        print(i, end = ' ')
    print()
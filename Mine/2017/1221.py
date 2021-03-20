for tc in range(1, int(input())+1):
    a, b = input().split()
    words = list(map(str, input().split()))
    e = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    print('#{}'.format(tc))

    for i in range(10):
        for l in words:
            if e[i] == l:
                print(l, end = ' ')
    print()
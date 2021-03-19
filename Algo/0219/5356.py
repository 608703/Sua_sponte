T = int(input())

for tc in range(1, T + 1):

    # 빈 리스트 생성
    arr = [0] * 5
    len_word = 0

    # 빈 리스트에 자료 추가
    for i in range(5):
        arr[i] = list(input())

        if len(arr[i]) > len_word:
            len_word = len(arr[i])

    print('#{}'.format(tc), end=' ')

    for i in range(len_word):
        for j in range(5):
            if len(arr[j]) > i:
                print(arr[j][i], end='')
    print()

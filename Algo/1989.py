for tc in range(1, int(input())+1):
    word = input()

    if word == word[::-1]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
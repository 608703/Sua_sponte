for tc in range(1, int(input())+1):
    word = input()
    mapp = input()

    result = 0
    for i in range(len(mapp) - len(word) + 1):
        if mapp[i:i+len(word)] == word:
            result = 1

    print('#{} {}'.format(tc, result))

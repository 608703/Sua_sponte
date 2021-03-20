for tc in range(1, int(input())+1):
    words = input()
    for s in range(1, 10):
        if words[:s] == words[s:2*s]:
            print('#{} {}'.format(tc, s))
            break
for tc in range(1, int(input())+1):
    words = input()
    len_d = len(words) # 갯수로 하나하나 점검해야하니 수 파악
    stack = []

    for i in range(len_d):
        # 비었거나 마지막 값이 다르면 추가
        if not stack or stack[-1] != words[i]:
            stack.append(words[i])
        # 안에 있는데 그게 같으면 제거
        elif stack and stack[-1] == words[i]:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))
for tc in range(1, int(input()) + 1):
    n = input()
    stack = []

    for i in range(len(n)):
        if n[i] == '{' or n[i] == '(':
            stack.append(n[i])
        elif n[i] == '}' or n[i] == ')':
            if len(stack) == 0:
                stack = [n[i]]
                break
            elif (n[i] == '}' and stack[-1] != '{') or (n[i] == ')' and stack[-1] != '('):
                stack = [n[i]]
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
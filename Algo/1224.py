for tc in range(1, 11):
    n = int(input())
    nums = input()

    stack = []
    numl = []

    icp = {'*': 2, '+': 1, '(': 3}
    isp = {'*': 2, '+': 1, '(': 0}

    for i in range(n):
        if nums[i].isdigit():
            numl.append(nums[i])
        else:
            if not stack: # 빈 경우
                stack.append(nums[i])
                continue
            elif stack: # 즉 비지 않은 경우
                if nums[i] == ')':
                    while stack[-1] != '(':
                        numl.append(stack.pop())
                    stack.pop()
                elif icp[nums[i]] > isp[stack[-1]]:
                    stack.append(nums[i])
                else:
                    while icp[nums[i]] <= isp[stack[-1]]:
                        numl.append(stack.pop())
                    stack.append(nums[i])

    for i in range(len(numl)):
        if numl[i].isdigit():
            stack.append(numl[i])
        else:
            two = int(stack.pop())
            one = int(stack.pop())

            if numl[i] == '+':
                result = one + two
            elif numl[i] == '*':
                result = one * two

            stack.append(str(result))
    print('#{} {}'.format(tc, stack[0]))
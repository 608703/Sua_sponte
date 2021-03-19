in_come_pri = {"*": 1, "/": 1, "-": 0, "+": 0}
in_stack_pri = {"*": 1, "/": 1, "-": 0, "+": 0}

for tc in range(1, 11):# 입력값 항상 잘 보면서 짜기
    n = int(input())
    nums = input()
    stack = []
    fornums = []
    # 전체 순회
    for i in range(len(nums)):
        trash = nums[i]
        # 연산자일 경우
        if trash in {"*", "+", "-", "/"}: # 문제에 곱 더하기 만 있다는데 구라다. 다 해줘야한다 keyerror 뜬다...
            if not stack or in_come_pri[trash] > in_stack_pri[stack[-1]]:
                stack.append(trash)
            else:
                while stack and in_come_pri[trash] <= in_stack_pri[stack[-1]]:
                    fornums.append(stack.pop())
                stack.append(trash)
        # 숫자일 경우 추가
        else:
            fornums.append(int(trash))

    if stack:
        while stack:
            fornums.append(stack.pop())
    for i in range(len(fornums)): # 계산 시작
        if type(fornums[i]) == int: # 이미 숫자인건 isdecimal 안 먹힘 다시 숙지, 문자열이 숫자인지 점검
            stack.append(fornums[i])
        else:
            frontline = stack.pop()
            endline = stack.pop()
            if fornums[i] == '+':
                frontline += endline
            elif fornums[i] == '*':
                frontline *= endline
            elif fornums[i] == '/':
                frontline /= endline
            else:
                frontline -= endline

            stack.append(frontline)
    print('#{} {}'.format(tc, stack.pop()))
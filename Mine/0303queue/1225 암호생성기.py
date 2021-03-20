for i in range(1, 11):
    tc = int(input())
    mapp = list(map(int, input().split()))

    time = 0  # 횟수
    maker = 1 # 하나씩 빼줄거
    while time < 6:
        pwd = mapp.pop(0) # 앞에 놈 데려와서
        pwd -= maker      # 빼주고
        if pwd <= 0:       # 0보다 작을 경우 어떻게 할지 조건주고
            pwd = 0
            mapp.append(pwd)
            break
        mapp.append(pwd)
        # 하나씩 더 해주고
        time += 1
        maker += 1
        if maker == 6: # 한바퀴 돌았으면 원위치
            time = 0
            maker = 1
    print('#{}'.format(tc), end = ' ')
    for i in mapp:
        print(i, end = ' ')
    print()
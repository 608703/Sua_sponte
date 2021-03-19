A,B = map(int, input().split())
if A == 1 and B == 2:
    print('B')
elif A == 1 and B == 3: # 가위 보
    print('A')
elif A == 2 and B == 1: # 바위 가위
    print('A')
elif A == 2 and B == 3: # 바위 보
    print('B')
elif A == 3 and B == 1: # 보 가위
    print('B')
elif A == 3 and B == 2: # 보 바위
    print('A')
for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    NUM = 12
    result = 0
    for i in range(1 << NUM):
        # i의 비트 표현이 부분집합을 나타냄
        cnt = 0
        sum_v = 0
        for j in range(NUM):
            # j번째 비트가 1인지 확인
            # 부분집합의 개수가 N개인지 확인, 총합
            if i & (1 << j):
                cnt += 1
                sum_v += j + 1
        # cnt 와 sum_v의 값이 조건에 맞으면 개수 증가
        if cnt == n and sum_v == k:
            result += 1

    print("#{} {}".format(tc, result))
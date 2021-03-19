def finder(v):
    # queue 준비
    queue = []

    # 추가, 방문
    queue.append(v)
    visited[v] = 1

    # 당연히 제일 전방부터
    while queue:
        v = queue.pop(0)
        for i in range(e):
            if list1[i][0] == v and visited[list1[i][1]] == 0:
                so = list1[i][1]
                queue.append(so)
                distance[so] = distance[v] + 1 # 다음걸 해줘야 하므로
                visited[so] = 1

            if list1[i][1] == v and visited[list1[i][0]] == 0:
                so = list1[i][0]
                queue.append(so)
                distance[so] = distance[v] + 1
                visited[so] = 1

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(e)]
    head, tail = map(int, input().split())
    distance = [0] * (v + 1) # 거리
    visited = [0] * (v + 1)  # 방문
    finder(head)

    print('#{} {}'.format(tc, distance[tail]))
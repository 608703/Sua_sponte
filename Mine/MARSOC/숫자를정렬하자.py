T = int(input())


def selection_sort(a, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, N)

    print("#{}".format(tc), end=" ")
    for i in range(N):
        print(arr[i], end=" ")
    print()
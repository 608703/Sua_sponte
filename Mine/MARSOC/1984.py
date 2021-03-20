for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    result = round((sum(nums) - max(nums) - min(nums)) / 8)

    print('#{} {}'.format(tc, result))
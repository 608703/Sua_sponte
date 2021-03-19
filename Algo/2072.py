import sys
sys.stdin = open('2072.txt')

T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    result = 0
    for number in numbers:
        if number % 2:
            result += number

    print('#{} {}'.format(test_case, result))
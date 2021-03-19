import sys
sys.stdin = open('2068.txt')

T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number

    print('#{} {}'.format(test_case, max_number))
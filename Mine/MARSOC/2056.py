T = int(input())

for test_case in range(1, T + 1):
    date = input()
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(year) < 0:
        print(f'#{test_case} -1')
    else:

        if (int(month) > 12) or (int(month) == 0):
            print(f'#{test_case} -1')
        else:
            if (int(day)) > month_day[int(month)-1] or (int(day) == 0):
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {year}/{month}/{day}')
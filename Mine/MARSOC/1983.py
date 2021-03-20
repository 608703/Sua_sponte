for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scores = []

    for i in range(n):
        a, b, c = map(int, input().split())

        scores.append(0.35 * a + 0.45 * b + 0.2 * c)

    kscore = scores[k - 1]

    scores.sort(reverse=True)

    kgrade = int(scores.index(kscore) / (n // 10))
    print('#{} {}'.format(tc, grade[kgrade]))
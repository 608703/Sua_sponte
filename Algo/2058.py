N = int(input())
result = 0

for i in range(0, len(str(N))):
    result += N % 10
    N //= 10
print(result)
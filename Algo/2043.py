a, b = map(int, input().split())

result = 1

while True:
    b += 1
    result += 1
    if a == b:
        break
print(result)
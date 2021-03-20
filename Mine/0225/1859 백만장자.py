import sys
sys.stdin = open('1859.txt')

for tc in range(1, int(input())+1):
    n = int(input())
    prices = list(map(int, input().split())) # 쭉 비교해야되니 list
    result = 0

    price = prices[n-1] # 최고가 앞에 가격들을 사서 고가에 팔아야되니 최후방 잡기
    for i in range(n-1, -1, -1): # 뒤에서 쭉 돌려줘서 최고가 잡고 앞에 잔챙이들 최고가에 빼기
        if prices[i] >= price:
            price = prices[i]
        result += (price - prices[i]) # 최고가 잡고 쭉 빼서 더해주기
    print('#{} {}'.format(tc, result))
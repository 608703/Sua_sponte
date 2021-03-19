T = int(input())
list1 = list(map(int, input().split()))
list1.sort()
print(list1[len(list1)//2])
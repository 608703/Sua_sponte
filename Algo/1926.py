num = int(input())

for i in range(1, num+1):
    s = sum(1 for i in str(i) if i in ['3','6','9'])
    if s==0:
        print( i, end=' ' )
    else:
        print( '-'*s, end=' ' )
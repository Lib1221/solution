n = int(input())
for i in range(n):
    k = int(input())
    num = list(map(int, input().split()))
    num.sort()
    z = 0
    for j in range(1, k):
        if num[j]-num[j-1] <=1:
            z = z
        else:
            z+=1
    value = "YES" if z==0 else "NO"
    print(value)

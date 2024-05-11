m, n = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
res = 0
result = []
l = 0
for i in num2:
    while l<len(num1) and num1[l] < i:
       res+=1
       l+=1
    result.append(res)
print(*result, sep=" ")

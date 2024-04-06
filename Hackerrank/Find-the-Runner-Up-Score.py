if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    a.sort()
    highest = len(a)-1
    x = a[0]
    for i in range(len(a)-1, 0, -1):
        if a[highest]>a[i]:
            print(a[i])
            break
    else:
        print(x)

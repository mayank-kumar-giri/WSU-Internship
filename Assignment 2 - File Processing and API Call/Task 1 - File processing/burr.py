t = int(input())
for i in range(t):
    s = 0
    n,q = map(int, input().split())
    arr = list(range(1,n+1))
    for j in range(q):
        t = list(map(int, input().split()))

        if t[0] == 1:
            y = t[1]
            x = y + s
            arr[x] = 0
        else:
            p,q = t[1], t[2]
            l = p + s - 1
            r = q + s
            ans = max(arr[l:r])
            s = (s+ans)%n
            print(ans)

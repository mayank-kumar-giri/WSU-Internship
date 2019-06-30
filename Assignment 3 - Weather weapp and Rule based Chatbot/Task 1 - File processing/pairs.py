t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = (sum(a) + sum(b))/2
    ae = 0
    be = 0
    for j in range(len(a)):
        if a[j]%2 == 0:
            ae += 1
        if b[j]%2 == 0:
            be += 1
    loss = (max(ae,be)-min(ae,be))/2
    ans = ans - loss
    print(int(ans))
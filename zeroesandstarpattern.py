n = int (input())
i = 1
while i<=n:
    j = 1
    while j<=2*n+1:
        if j==i or j==n+1 or j==2*n-i+2:
            print('*',end="")
        else:
            print('0',end="")
        j = j + 1
    print()
    i = i + 1

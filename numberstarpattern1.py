n = int(input())
i = 1
while i<=n:
    j=n
    while j>=1:
        if j!=i:
            print(j,end="")
        else:
            print('*',end="")
        j = j-1
    print()
    i = i +1

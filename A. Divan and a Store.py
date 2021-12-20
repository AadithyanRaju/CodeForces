#A. Divan and a Store
for _ in range(int(input())):
    n,l,r,k=map(int,input().split())
    an=list(map(int,input().split()))
    an=an[:n]
    se=[]
    for i in an:
        if r>=i and i>=l:
            se.append(i)
    se.sort()
    while sum(se)>k and len(se)!=0:se.pop()
    print(len(se))

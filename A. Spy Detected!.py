for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if l.count(l[i])<2:
            print(i+1)
            break
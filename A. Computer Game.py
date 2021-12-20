for a in range(int(input())):
    l=[]
    n=int(input())
    flag='YES'
    for b in range(2):l.append((input())[:n])
    for c in range(n):
        if l[0][c]==l[1][c]=='1':
            flag='NO'
    print(flag)
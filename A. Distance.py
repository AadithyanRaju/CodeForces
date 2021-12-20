def d(X,Y):
    x1=X[0]
    y1=X[1]
    x2=Y[0]
    y2=Y[1]
    dis=abs(x1-x2)+abs(y1-y2)
    return dis
A=[0,0]
for _ in ' '*int(input()):
    x,y=map(int,input().split())
    B=[x,y]
    AB=d(A,B)
    for i in range(int(AB/2+1)):
        x,y=i,abs(AB/2-i)
        C=[int(x),int(y)]
        BC=d(B,C)
        AC=d(A,C)
        if BC==AC:
            print(x,int(y))
            break
    else:print(-1,-1)
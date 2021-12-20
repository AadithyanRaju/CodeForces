t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())    
    l=[a,b,c]
    if a==b and b==c:
        print(1,1,1)
        continue
    if a>b and b>=c:
        print(0,a-b+1,a-c+1)
        continue
    if b>a and a>=c:
        print(b-a+1,0,b-c+1)
        continue
    if c>a and a>=b:
        print(c-a+1,c-b+1,0)
        continue
    if a<b and b==c:
        print(b-a+1,1,1)
        continue
    if b<a and a==c:
        print(1,a-b+1,1)
        continue
    if c<a and a==b:
        print(1,1,a-c+1)
        continue
    if c>b and b>=a:
        print(c-a+1,c-b+1,0)
        continue
    if b>c and c>=a:
        print(b-a+1,0,b-c+1)
        continue
    if a>c and c>=b:
        print(0,a-b+1,a-c+1)
        continue
    if c<b and b==a:
        print(1,1,b-c+1)
        continue
    if b<c and c==a:
        print(1,c-b+1,1)
        continue
    if a<c and c==b:
        print(c-a+1,1,1)
        continue
    

def p(z):return [x for x in range(1,z+1)]
for _ in ' '*int(input()):
    n,a,b=map(int,input().split())
    if n%2==1:
        print(-1)
    else:
        l,r=[a],[b]
        for i in p(n)[::-1]:
            if (i not in l) and (i not in r):
                if len(l)>=n/2:
                    r.append(i)
                else:
                    l.append(i)
        if min(l)==a and max(r)==b:
            print(*l,*r)
        else:print(-1)
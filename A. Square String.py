for _ in ' '*int(input()):
    x=input()
    if len(x)%2==0:
        y=x[:len(x)//2]
        if y*2==x:print('Yes')
        else:print('No')
    else:print('No')
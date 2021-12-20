t=int(input())
for a in range(t):
    l=[]
    x=input()
    for i in x:l.append(ord(i))
    m=l.index(min(l))
    y=chr(l.pop(m))
    x=''
    for i in l:x+=(chr(i))
    print(y,x)

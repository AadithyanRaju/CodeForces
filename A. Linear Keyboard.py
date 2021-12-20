for _ in range(int(input())):
    k,s=input(),input()
    print(sum(abs(k.index(s[i])-k.index(s[i+1])) for i in range(len(s)-1)))
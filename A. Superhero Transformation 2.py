a,b=input(),input()
if len(a)==len(b):
    for i in range(len(a)):
        if a[i] in 'AEIOUaeiou' and b[i] in 'AEIOUaeiou':f=True
        elif a[i] not in 'AEIOUaeiou' and b[i] not in 'AEIOUaeiou':f=True
        else:
            f=False
            break
else:f=False
print('Yes' if f else 'No')

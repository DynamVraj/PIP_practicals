'''
    20CS059
    VRAJ PATEL
'''
n=int(input())
for i in range(n):
    a=input()
    b=len(a)
    a1=a[:b//2]
    if(b%2==0):
        a2=a[b//2:]
    else:
        a2=a[b//2+1:]
    if(sorted(a1)==sorted(a2)):
        print("YES")
    else:
        print("NO")
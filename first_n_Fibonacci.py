n=int(input())
if n==1:
    print (0)
elif n==2:
    print (0)
    print (1)
else:
    print (0)
    print (1)
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print (c)

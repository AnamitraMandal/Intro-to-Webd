def GCD(a,b):
    if a%b==0:
        return b
    else:

       return GCD(b,a%b)
n1=int(input())
n2=int(input())
gcd=GCD(n1,n2)
print(gcd)

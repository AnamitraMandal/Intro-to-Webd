n1=int(input())
n2=int(input())
a=n1
b=n2
while a%b != 0:
    temp= b
    b = a % b
    a=temp

print(b)
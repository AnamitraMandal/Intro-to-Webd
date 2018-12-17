n=int(input("enter no of words"))
abbr=""
a=[]
for i in range(n):
    wd = input().split()
    for j in range(len(wd)):
        abbr+=wd[j][0]
    a.append(abbr)
    abbr=""
for i in range(n):
    print (a[i])
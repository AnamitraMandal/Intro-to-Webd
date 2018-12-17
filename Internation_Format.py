def insert_comma(string, index):
    if len(string)<4:
        return string
    else:
        return insert_comma(string[:index], -3) + ',' + string[index:]
n=int(input("Enter no of elements"))
l=[]
for i in range(n):
    ip = input()
    l.append(ip)
for i in range(n):
    print (insert_comma(l[i], -3))
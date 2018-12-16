my_order = {}
for i in range(int(input())):
    name,bk,price = input().rpartition(' ')
    if name not in my_order:
        my_order[name] = int(price)
    else:
        my_order[name] += int(price)
for name, price in my_order.items():
    print (name,price)
string = input()
c = 1
l = len(string)
#string[len] = ' '
for i in range(0, l-1):
    if string[i] == string[i + 1]:
        c += 1
        if i==(l-2):
            print("(", c, ",", string[i], ") ", end="")

    else:
        print ("(",c,",",string[i],") ",end="")

        c = 1
        if i==(l-2):
            print ("(",c,",",string[i+1],") ",end="")

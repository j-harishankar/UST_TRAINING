i = 1
j = 1
for i in range(7):
    print("*"*i)
    i+=1
for i in range(7,1,-1):
    print(" "*(i-1),end=" ")
    print("*"*j)

    j+=1
def diamond(n):

    for i in range(n):
        print("*"*i)
    for j in range(n,0,-1):
        print("*"*j)
diamond(5)


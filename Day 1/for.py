l = ['LOYOLA']
for f in l:
    for i in f:
        print(i,end = "     ")
    k = len(f)-1
    print(" ")
    for i in range(k+1):
        print(k,end="     ")
        k-=1

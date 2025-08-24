for f in range(1,31):
    if f%4!=0:
        if f%10==0:
            print(f,end=" ")
        else:
            print(f, end='-')
    if f%10 == 0:
        print(" ")


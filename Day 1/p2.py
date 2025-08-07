i = 5
k=0
while i!=0:
    j = i+10
    while j>=11:
        if j == 11:
            print(j+k,end = " ")
        else:
            print(j+k,end=", ")
        j -= 1
    k += 10
    if k ==50:
        print(" ")
    else:
        print("**",end= " ")
    i-=1
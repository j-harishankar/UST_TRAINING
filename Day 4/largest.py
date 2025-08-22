def largest(l):
    maxi = 0
    for i in range(1,len(l)):
        if l[i-1]>l[i]:
            maxi = l[i-1]
        else:
            maxi = l[i]
    return maxi
l = [12,34,54,6,787,3]
print(largest(l))
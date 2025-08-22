def lof(n1,n2):
    return max(n1,n2)
n1 = int(input("n1"))
n2 = int(input("n2"))
s = lof(n1,n2)
ladd = lambda n1,n2 : n1 + n2
print("Sum of lambda ==>",ladd(n1,n2))
def rev(stri):
    strii = " "
    n = len(stri)-1
    for i in range(len(stri)):
        print(i)
        strii+=stri[n-i]
    return strii

print(rev("dff"))



print(s)

def sum(n):
    x = n%2
    if n==1:
        return 1
    #print(n,end="\n")
    return n+sum(n-1)

a = int(input("Enter A Number: "))
n = a
su = 0
while(n>0):
    # if(n%2==0):
    if(n%2!=0):
        print(n,end="\n")
        su = su + n
    n = n-1
print(su)
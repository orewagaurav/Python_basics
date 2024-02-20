n = int(input("Enter a number: "))
t = n  # this is quite neccessary
s = 0    
p = str(n)
x = len(p)
while(t>0):
    rem = t%10
    s = (s*10) + rem
    t//=10

if(s == n):
    print("Plaindrome Hai!")
else:
    print("Plaindrome Nhi Hai!")
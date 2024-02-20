n = int(input("Enter a number: "))
t = n  # this is quite neccessary
s = 0    
p = str(n)
x = len(p)
while(t>0):
    rem = t%10
    s = s + (rem**x)
    t//=10

if(s == n):
    print("Armstrong Hai!")
else:
    print("Armstrong Nhi Hai!")


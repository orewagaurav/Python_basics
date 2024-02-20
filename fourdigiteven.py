n = input("")
p = str(n)
while(len(p) == 4):
    a = int(p[0])
    b = int(p[3])
    
    if(a%2==0 and b%2==0):
        print("True")
        break
    else:
        print("False")
        break
else:
    print("Wrong Number! Enter four digit number!")
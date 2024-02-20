#multiple input

# a,b,c = input("a,b,c: ").split(",")
# print(a,b,c,sep="\n")

#prime numbers

a = int(input("Enter lower bound: "))
b = int(input("Upper bound: "))
flag = 0 #False ko bhi use kr skte hai

for i in range(a,b+1):
    if(i==1):
        continue
    flag = 1 #True ko bhi use kr skte hai, iska mtlb prime number hai!
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=0 #iska mtlb prime number nhi hai!
            break

    if flag:
        print(i,end = "\n")
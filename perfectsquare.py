a = int(input("Enter a lower bound: "))
b = int(input("Enter a upper bound: "))

for i in range(a,b+1):
    if int(i**0.5)**2 == i:
        print("Perfect square...")
        break
    print(i, end = "\n")
a = input("Enter a number: ")
print("Reverse of a is: ", a[::-1])
if a==a[::-1]:
    print("palindrome....")
else:
    print("Not palindrome....")
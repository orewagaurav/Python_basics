def sum(no):
    if (no==1):  #base condition
        return 1
    else:
        return(no + sum(no-1))  #logic/recursion
    
def start():
    last = input("Enter the last number: ")
    last = int(last)
    total = sum(last)
    print("The sum of the series from 1 to", last, "is", total)
    
start()
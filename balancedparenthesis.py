para = input("Enter the brackets: ")
op, cl = 0,0
for i in para:
    if i == '(':
        op+=1
    elif i == ')':
        cl+=1
        
if op==cl: print("Balanced")
else: print("Unbalanced..")
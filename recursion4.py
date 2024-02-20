def fun(n):
    if(n>0):
        print(n, end=" ")
        # last statement in the function 
        fun(n-1)

#Driver code
x = 30
fun(x)
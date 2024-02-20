def fun(n):
    if(n>0):
        fun(n-1)
        print(n, end="\n")
        
x=30 
fun(x)
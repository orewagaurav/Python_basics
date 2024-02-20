square_func = lambda x : x**2
print(square_func(4))

close_enough = lambda x,y : abs(x-y) < 3
print(close_enough(2,4)) 

def get_func(n):
    return lambda x : x * n + x % n
my_func = get_func(13)
print(my_func(4))
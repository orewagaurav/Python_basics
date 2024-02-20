ls = [6,8,10,12,13,19,5,18]
x = lambda y:y**2
even = lambda z:z if z%2==0 else 0
m = list(map(x,ls))
li = list(map(even,ls))
print(m)
print(li)
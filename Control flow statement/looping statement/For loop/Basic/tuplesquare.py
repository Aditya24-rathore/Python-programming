# WAP to square a tuple element
n=(1,2,3,4,5)
new_tup=[]
for i in n:
    new_tup.append(i**2)
print(tuple(new_tup))
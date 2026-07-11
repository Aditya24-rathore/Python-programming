import keyword

x=keyword.kwlist
print(x)
print(len(x))  # 35

y=keyword.softkwlist
print(y)
print(len(y))  # 0

z=keyword.iskeyword('if')
print(z)  # True
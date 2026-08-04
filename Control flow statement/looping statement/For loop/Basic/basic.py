# Reverse a string
s="aditya"
s1=s[::-1]
print(s1)

# Reverse a list
l=[1,2,3,4,5]
l1=[]
for i in range(len(l)-1, -1, -1):
    l1.append(l[i])
print(l1)
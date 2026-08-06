# WAP to reverse a interger value
n=12345
rev=0
while n>0:
    l_d=n%10
    rev=l_d+rev*10
    n=n//10
print(rev)
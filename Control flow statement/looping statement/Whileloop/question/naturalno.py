n=int(input('enter a number'))
i=1
while i<=n:
    print(i,end=' ')
    i=i+1  #1 2 3 4 5


n=int(input('enter a number'))
i=1
while i<=n:
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+1  

n=int(input('enter a number'))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print('Sum of natural numbers:', sum)

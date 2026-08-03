# WAP to print even numbers upto numbers
# n=int(input('enter a number : '))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         if i<n:
#             print(i,end='+')
#         else:
#             print(i,end='=')
#     i=i+1
    

# n=int(input('enter  a number:'))
# i=1
# sum=0
# while i<n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print('Sum of even numbers:',sum)

#Even number upto n number
n=int(input('enter a number : '))
i=1
while i<=n:
    print(i)
    i=i+1

n=int(input('enter a number : '))
i=1
while i<=n:
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+1
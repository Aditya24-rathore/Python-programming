n=int(input('enter a value'))
n_len=0
while n>0:
    n_len=n_len+1
    n=n//10
print('length of a value is :' , n_len)
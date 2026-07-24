# Typecasting:-Converting one datatype into another
# Python inbuilt function for typecast:- int,float,complex,str,list,tuple,dict,set,fset

# 1. convert int data type to another data type
x=10
print(float(x)) #10.0
print(complex(x))  #(10+0j)
print(str(x)) #10
print(list(x)) #TypeError: 'int' object is not iterable
print(tuple(x)) #TypeError: 'int' object is not iterable
print(dict(x)) #TypeError: 'int' object is not iterable
print(set(x)) #TypeError: 'int' object is not iterable
print(frozenset(x)) #TypeError: 'int' object is not iterable

#2. convert str into another data type
x='python'
print(float(x)) #valueError: could not convert string to float: 'python' 
print(complex(x))  #ValueError: complex() arg is a malformed string 
print(int(x)) #ValueError: invalid literal for int() with base 10: 'python' 
print(list(x)) #['p', 'y', 't', 'h', 'o', 'n']
print(tuple(x)) #('p', 'y', 't', 'h', 'o', 'n')
print(dict(x)) #TypeError: 'int' object is not iterable
print(set(x)) #{'y', 't', 'o', 'n', 'h', 'p'}
print(frozenset(x)) #frozenset({'y', 't', 'o', 'n', 'h', 'p'}) 

#3. List into another data type
x=[10,20,'python','java']
print(int(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list' 
print(str(x)) #[10, 20, 'python', 'java']
print(tuple(x)) #(10, 20, 'python', 'java')
print(set(x)) #{'java', 'python', 10, 20}
print(frozenset(x)) #frozenset({10, 20, 'java', 'python'})
print(dict(x)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence 

#4. dict into another data type
x={'name':'aditya','age':20}
print(frozenset(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(set(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(tuple(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(list(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(str(x)) #{'name': 'aditya', 'age': 20}
print(int(x)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
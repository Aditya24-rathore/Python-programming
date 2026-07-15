'''Dictionary in python :-
1.Collection of key-value pairs is called dictionary.
2.Dictionary is mutable, meaning once they are created, their content can be changed.
3.Keys in a dictionary must be unique and immutable.
4.Values in a dictionary can be of any data type and can be duplicated.
5.Enclosed in curly braces { } and key-value pairs are separated by commas.
6.Key is always a immutable data type (string, number, tuple) and value can be any data type (string, number, list, tuple, dictionary).
7.Due to unordered collection, we cannot access the elements of a dictionary using indexing and slicing.
Indexing and slicing is not possible in dictionary because it is unordered collection.
key and value are separated by colon(:) in dictionary.'''

# Python inbuilt function for dictionary
d={'name':'aditya','age':20,'city':'pune'}
print(d)
print(type(d))  # <class 'dict'>
print(len(d))  # 3
print(max(d))  # name
print(min(d))  # age            
print(id(d))  # Memory address of the dictionary
print(sum(d))  # TypeError: unsupported operand type(s) for +: 'int' and 'str' because we cannot add different data types.

d1={'name':'aditya','age':20,'city':'pune','name':'aditya',1:'aditya'}  # Duplicate key is not allowed in dictionary and it will take the last value of the duplicate key.
print(d1)  # {'name': 'aditya', 'age': 20, 'city': 'pune'} because key must be unique in dictionary and it will take the last value of the duplicate key.
print(min(d1))  # 1 because key must be unique in dictionary and it will take the last value of the duplicate key.
print(max(d1))  # name because key must be unique in dictionary and it will take the last value of the duplicate key.
print(sum(d1))  # TypeError: unsupported operand type(s) for +: 'int' and 'str' because we cannot add different data types.

# Dictionary method:-
d={'name':'aditya','age':20,'city':'pune'}
#1. copy() method:- copy() method is used to create a shallow copy of the dictionary.
d1=d.copy()
print(d1)  # {'name': 'aditya', 'age': 20, 'city': 'pune'}
print(id(d))  # Memory address of the dictionary
print(id(d1))  # Memory address of the dictionary both are different because copy() method creates a shallow copy of the dictionary.

#2. clear() method:- clear() method is used to remove all the elements from the dictionary.
d={'name':'aditya','age':20,'city':'pune'}
d.clear()
print(d)  # {}

#3. fromkeys() method:- if you gave a value they make value with key and add a value none
l=['name','age','city']
d=dict.fromkeys(l)
print(d)   #{'name': None, 'age': None, 'city': None}
d=dict.fromkeys(l,"aditya")
print(d)  #{'name': 'aditya', 'age': 'aditya', 'city': 'aditya'}

#4. keys() method :- it give all the key of the dict
d={'name':'aditya','age':20,'city':'bhopal'}
print(d.keys()) #(['name', 'age', 'city']) it give keys in list

#5. values() method:- it give all the key of the dict
d={'name':'aditya','age':20,'city':'bhopal'}
print(d.values()) #(['aditya', 20, 'bhopal']) it give values in list

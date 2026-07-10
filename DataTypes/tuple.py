'''Tuple in python :-
1.Collection of element (homogenous(means same data type) or heterogeneous(means different data types)) is called tuple.
2.Tuple is immutable, meaning once they are created, their content cannot be changed.
3.Ordered Collection
4.Tuple can contain duplicate elements.
5.Enclosed in parentheses () and elements are separated by commas.
6.Due to ordered collection, we can access the elements of a tuple using indexing and slicing.
7. Tuple is faster than list because it can take less memory and it is immutable.'''


# Python inbuilt function for tuple
t=(1,2,3,4,5)
print(t)
print(type(t))  # <class 'tuple'>
print(len(t))  # 5
print(max(t))  # 5 and it cannot compared with heterogeneous data types because it is immutable.
print(min(t))  # 1
print(id(t))  # Memory address of the tuple
print(sum(t))  # 15
print(t[0])  # 1

# Tuple method:- Only two methods are available for tuple because it is immutable.
# 1. count() method:- count() method is used to count the number of occurrences of an element in the tuple.
t=(1,2,3,4,5,1,2,3,4,5)
print(t.count(1))  # 2
print(t.index(1))  # 0


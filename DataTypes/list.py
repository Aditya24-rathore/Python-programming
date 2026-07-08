'''List in python :-
1.Collection of element (homogenous(means same data type) or heterogeneous(means different data types)) is called list.
2.List is mutable, meaning once they are created, their content can be changed.
3.Ordered Collection
4.List can contain duplicate elements.
5.Enclosed in square brackets [ ] and elements are separated by commas.
6.Due to ordered collection, we can access the elements of a list using indexing and slicing.'''

l1=[1,2,3,4,5]
l2=['Python','Java','C++','C#']
l3=[1,2,3,'Python','Java',4.5,True]

# Python inbuilt function for list
print(l1,l2,l3)

# 1.Length of the list
print(len(l1))  # Length of the list
print(len(l2))  # Length of the list
print(len(l3))  # Length of the list

# 2.Maximum and Minimum element in the list
print(max(l1))  # 5
print(max(l2))  # Python
print(max(l3))  # TypeError: '>' not supported between instances of 'str' and 'int'
print(min(l1))  # 1
print(min(l2))  # C#
print(min(l3))  # TypeError: '<' not supported between instances of 'str' and 'int' type error in heterogeneous list because we cannot compare different data types.

# 3. Memory address of the list (id)
print(id(l1))  
print(id(l2))
print(id(l3))

# 4. Type of the list
print(type(l1))  # <class 'list'>
print(type(l2))  # <class 'list'>
print(type(l3))  # <class 'list'>   

# sum of the list
print(sum(l1))  # 15
print(sum(l2))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum(l3))  # TypeError: unsupported operand type(s) for +: 'int' and 'str' type error in heterogeneous list because we cannot add different data types.


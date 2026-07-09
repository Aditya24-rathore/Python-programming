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

# List method:-
# 1. Append method:- append() method is used to add an element at the end of the list.
l=[1,2,3,4,5]
l1="python"
l2=[1,2,3,4,5]
l3=4
l.append(l2)
l.append(l1)
l.append(l3)
print(l)  # [1, 2, 3, 4, 5, 'python']
print(l) #[1, 2, 3, 4, 5, [1, 2, 3, 4, 5], 'python']
print(l)  # [1, 2, 3, 4, 5, [1, 2, 3, 4, 5], 'python', 4]

# 2. Extend method:- extend() method is used to add multiple elements at the end of the list.
l=[1,2,3,4,5]
l1="python"
l2=["python"]
l3=1
l.extend(l)
print
l.extend(l1)
print(l)  # [1, 2, 3, 4, 5, 'p', 'y', 't', 'h', 'o', 'n']
l.extend(l2)
print(l)  # [1, 2, 3, 4, 5, 'p', 'y', 't', 'h', 'o', 'n', 'python']
l.extend(l3)
print(l)  # TypeError: 'int' object is not iterable


# 3. Insert method:- insert() method is used to add an element at a specific index in the list.
l=[1,2,3,4,5]
l1="python"
l2=[15,20]
l.insert(2, l1)
print(l)  # [1, 2, 'python', 3, 4, 5]
l.insert(3,l2)
print(l)  # [1, 2, 'python', [15, 20], 3, 4, 5]
l.insert(0,"aditya")
print(l)  # ['aditya', 1, 2, 'python', [15, 20], 3, 4, 5]
l.insert(30,"aditya")
print(l) # ['aditya', 1, 2, 'python', [15, 20], 3, 4, 5, 'aditya']  # if index is greater than the length of the list, then the element will be added at the end of the list.

# 4. count method:- count() method is used to count the number of occurrences of an element in the list.
l=[1,2,3,4,5,1,2,3,4,5]
print(l.count(1))  # 2
l1=[1,2,3,4,[1,2]]
print(l1.count(1))  # 1 
l2=[1,2,3,4,5]
print(l2.count(6))  # 0  # if the element is not present in the list, then the count will be 0.

# 5. clear method:- clear() method is used to remove all the elements from the list.
l=[1,2,3,4,5]
print(l.clear())  # None
print(l)  # []  # after clearing the list, the list will be empty.

# 6. copy method:- copy() method is used to create a shallow copy of the list.
l=[1,2,3,4,5]
l2=l.copy()
print(l2)  # [1, 2, 3, 4, 5]

# 7. index method:- index() method is used to find the index of an element in the list.
l=[1,2,3,4,5]
print(l.index(3))  # 2
l1=[1,2,3,4,[1,2]]  
print(l1.index([1,2]))  # 4  # if the element is present in the list, then the index of the first occurrence of the element will be returned.
l2=[1,2,3,4,5]
print(l2.index(6))  # ValueError: 6 is not in list  # if the element is not present in the list, then ValueError will be raised.

l3=[1,2,3,4,5,1,2,3,4,5]
print(l3.index(1))  # 0  # if the element is present in the list, then the index of the first occurrence of the element will be returned.


# 8. pop method:- pop() method is used to remove and return the last element from the list. And remove element from the list at the specified index. If index is not specified, then the last element will be removed and returned.
l=[1,2,3,4,5]
print(l.pop())  # 5
print(l)  # [1, 2, 3, 4]

l1=[1,2,3,4,5]
print(l1.pop(2))  # 3
print(l1)  # [1, 2, 4, 5]


# 9. remove method:- remove() method is used to remove the first occurrence of an element from the list. If the element is not present in the list, then ValueError will be raised.
l=[1,2,3,4,5]
l.remove(3)
print(l)  # [1, 2, 4, 5]

l1=[1,2,3,4,5,1,2,3,4,5]
l1.remove(1)    
print(l1)  # [2, 3, 4, 5, 1, 2, 3, 4, 5]  # only the first occurrence of the element will be removed.

l2=[1,2,3,4,5]
l2.remove(6)  # ValueError: list.remove(x): x not in list  # if the element is not present in the list, then ValueError will be raised. 
print(l2)  # [1, 2, 3, 4, 5]  # the list will remain unchanged if the element is not present in the list.


# 10. reverse method:- reverse() method is used to reverse the elements of the list.
l=[1,2,3,4,5]
l.reverse()
print(l)  # [5, 4, 3, 2, 1]


# 11. sort method:- sort() method is used to sort the elements of the list in ascending order. If reverse=True is specified, then the elements will be sorted in descending order.
l=[5,4,3,2,1]
l.sort()    
print(l)  # [1, 2, 3, 4, 5]

l1=["Python","Java","C++","C#"]
l1.sort()
print(l1)  # ['C#', 'C++', 'Java', 'Python']


l2=[2,"Python",3,1,4]
l2.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'  # if the list contains different data types, then TypeError will be raised.
''' set in python:- 
1. collection of unordered elements.
2.mutable in nature
3.collection of unique element
4.enclosed with {} and elements are seperated by comma()
5. indexing and slicing not supported due to unordered collection
6.Duplicates not aloowed 
'''
# Python inbuilt function for set
'''s={10,20,"python","java"}
print(s) #{10, 'python', 20, 'java'}
print(type(s)) #<class 'set'>
print(len(s)) #4
print(id(s)) #2255125480160
#min,max,sum can be done in homogenous data type
print(min(s)) #TypeError: '>' not supported between instances of 'int' and 'str'
print(max(s)) #TypeError: '>' not supported between instances of 'int' and 'str'
print(sum(s)) #TypeError: '>' not supported between instances of 'int' and 'str' '''

# Set methods:- 
# 1. union():-
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}


# 2. intersection():-
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
print(s1.intersection(s2)) #{5, 6}

# 3. difference():-
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
print(s1.difference(s2)) #{1, 2, 3, 4}
 
# 4. symmetric_difference():-
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
print(s1.symmetric_difference(s2)) #{1, 2, 3, 4, 7, 8, 9}


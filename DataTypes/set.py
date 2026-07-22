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

# Method which can be performed on single set 
# 5. copy():-
s={'python','java',10,15}
s1=s.copy()
print(s1,s,sep=',')
print(id(s),id(s1)) #Both memory address are different

#6. clear:-
s={'python','java'}
s.clear()
print(s) #set()

# 7. remove():- remove is used to delete the element by targeting they give error if element is not in the set
s={10,20,29,20}
s.remove(20)
# s.remove(30) #KeyError: 30
print(s) #{10, 29} it remove 20 an it cannot allow dublicate only single 20 in the set

# 8. discard():- discard is used to delete the element by targeting they does not give error if element is not in the set
s={10,20,29,20}
s.discard(20)
s.discard(30) #does not give error
print(s) #{10, 29} it remove 20 an it cannot allow dublicate only single 20 in the set


# 9. pop():- remove the single element randomly due to unordered collection dont have indexing
s={10,20,30,40,50}
s.pop()
print(s) #{20, 40, 10, 30} remove 50 randomly

# 10 add():- add the single element ina set
s={10,'python',20}
s.add('java')
print(s) #{'python', 10, 20, 'java'}
s.add((10,20))
print(s) #{'java', 10, 'python', (10, 20), 20}
# s.add([10,20])
print(s) #TypeError: unhashable type: 'list does not add list because it has mutable

#11. update():- Add multiple element in a set
s={10,20,'java'}
s.update("python")
print(s) #{'t', 'n', 10, 'o', 20, 'p', 'h', 'y','java'}
s.update(('cpp','html',30))
print(s) #{'y', 'o', 10, 'cpp', 20, 30, 'java', 'n', 'h', 't', 'html', 'p'}
s.update([40,50])
print(s) #{'cpp', 'o', 'h', 40, 10, 50, 20, 'p', 't', 'html', 'y', 'n', 'java', 30}
''' frozenset in python:- 
1. collection of unordered elements.
2.immutable in nature
3.collection of unique element
4.enclosed with {} and elements are seperated by comma(,)
5. indexing and slicing not supported due to unordered collection
6.Duplicates not aloowed 
'''
l=[10,20,30,40]
t=('python','java',20,30)
s='python'
d={'name':'aditya','age':21}
fs1=frozenset(l)
fs2=frozenset(t)
fs3=frozenset(s)
fs4=frozenset(d)
print(fs1)  #frozenset({40, 10, 20, 30})
print(fs2) #frozenset({'java', 20, 'python', 30})
print(fs3) #frozenset({'h', 't', 'n', 'y', 'o', 'p'})
print(fs4) #frozenset({'name', 'age'})
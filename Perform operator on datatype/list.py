#1. Assignment operator
# a. Addition operator
l1=['java','python','cpp']
l2=['js','html','react']
l3=l1+l2
print(l3) #['java', 'python', 'cpp', 'js', 'html', 'react']

l1=[1,2,3]
l2=[3,4,5]
l3=l1+l2
print(l3) #[1, 2, 3, 3, 4, 5]

l1=[1,2,'java']
l2=['java','1']
l3=l1+l2
print(l3) #[1, 2, 'java', 'java', '1']


#b. subtraction operator:-SO basically subtraction operator cant perform on list
l1=['java','python','cpp']
l2=['js','html','react']
l3=l1-l2
print(l3) #unsupported operand type(s) for -: 'list' and 'list'

#c. multiplication operator:-SO basically multiplication operator cant perform on list
l1=['java','python','cpp']
l2=['js','html','react']
l3=l1*l2
print(l3) #can't multiply sequence by non-int of type 'list'
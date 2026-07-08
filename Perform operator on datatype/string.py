# Arithmetic operator on string datatype
s1="Aditya"
s2=2
s3="Python"

'''so basically we can only perform addition and multiplication operator on string datatype. Other operators will give type error because they are not supported on string datatype.'''


# 1.Addition operator (+) on string datatype
print(s1+s2)  # TypeError: can only concatenate str (not "int") to str
print(s1+s3)  # AdityaPython

# 2. Multiplication operator (*) on string datatype
print(s1*s2)  # AdityaAditya
print(s1*s3)  # TypeError: can't multiply sequence by non-int of type 'str'

# 3. Division operator (/) on string datatype
print(s1/s2)  # TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(s1/s3)  # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# 4. Subtraction operator (-) on string datatype
print(s1-s2)  # TypeError: unsupported operand type(s) for -: 'str' and 'int'
print(s1-s3)  # TypeError: unsupported operand type(s) for -:

# 5. Floor division operator (//) on string datatype
print(s1//s2)  # TypeError: unsupported operand type(s) for //: 'str' and 'int'
print(s1//s3)  # TypeError: unsupported operand type(s) for //: 'str' and 'str'

# 6. Modulus operator (%) on string datatype
print(s1%s2)  # TypeError: unsupported operand type(s) for %: 'str' and 'int'
print(s1%s3)  # TypeError: unsupported operand type(s) for %: 'str' and 'str'

# 7. Exponent operator (**) on string datatype
print(s1**s2)  # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
print(s1**s3)  # TypeError: unsupported operand type(s) for **
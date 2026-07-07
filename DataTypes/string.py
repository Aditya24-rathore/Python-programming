'''String:-
1. A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ") or triple quotes (''' ''' or """ """).
2. Strings can contain letters, numbers, symbols, and whitespace characters.
3. Strings are immutable, meaning once they are created, their content cannot be changed.
4.Ordered Collection: Strings maintain the order of characters, allowing for indexing and slicing.'''


s="Python"
 # Python inbuit function for string
print(s)  
print(len(s))  # Length of the string
print(max(s))  # Maximum character in the string
print(min(s))  # Minimum character in the string
print(id(s))  # Memory address of the string
print(ord('P'))  # Convert character to its ASCII value
print(chr(80))  # Convert ASCII value to its corresponding character
print(type(s))  # Type of the string

# String Method
m="thIs is Python cLass"
print(m.upper())  # Convert string to uppercase
print(m.lower())  # Convert string to lowercase
print(m.title())  # Convert string to title case
print(m.capitalize())  # Convert string to capitalize case
print(m.swapcase())  # Swap the case of each character in the string
print(m.count('i'))  # Count the occurrences of a substring in the string and count the number of times 'i' repeat in the string
print(m.startswith('th'))  # Check if the string starts with a specific substring gives true or false
print(m.endswith('ss'))  # Check if the string ends with a specific substring gives true or false
print(m.find('Python'))  # Find the index of the first occurrence of a substring in the string if the string is not found it will return -1
print(m.replace('Python', 'Java'))  # Replace a substring with another substring in the string  
print(m.isalpha())  # Check if all characters in the string are alphabetic gives true or false
print(m.isdigit())  # Check if all characters in the string are digits gives true or false
print(m.isalnum())  # Check if all characters in the string are alphanumeric gives true or false it does not contain any special characters or spaces
print(m.index('Python'))  # Find the index of the first occurrence of a substring in the string if the string is not found it will raise an error
# the difference between find and index is that find returns -1 if the substring is not found, while index raises a ValueError.(substring not found)

# Important String Methods
# split or join
# split() method is used to split a string into a parts and give output in the form of a list. In split we give two parameters first is the separator and second is the maximum number of splits to be done. If we do not give any separator then it will consider space as a separator.
a="Python is a programming language"
print(a.split()) #['Python', 'is', 'a', 'programming', 'language'] if we did not give any separator then it will consider space as a separator.
print(a.split('a')) #['Python is ', ' progr', 'mming l', 'ngu', 'ge'] if we give a separator then it will split the string at that separator.
print(a.split('a', 2)) #['Python is ', ' progr', 'mming language'] if we give a separator and maximum number of splits then it will split the string at that separator and will do the maximum number of splits.

# Join() method is used to join the elements of a list into a string. In join we give one parameter which is the list to be joined. The separator is the string on which we call the join method.
# In join we give one parameter which is the list to be joined. The separator is the string on which we call the join method.
s1="Python"
s2="Java"
l=[s1,s2]
print(' '.join(s1,s2))  # error:- str.join() takes exactly one argument (2 given)
print(' '.join(l))
print('-'.join([s1,s2]))  # Python-Java

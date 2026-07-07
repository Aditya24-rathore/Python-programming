'''Input() Function in Python is used to take input from the user. It reads a line from input, converts it into a string (stripping a trailing newline), and returns that. The by default, the input() function takes input as a string. If you want to take input of a different data type, you need to convert it explicitly.'''

s=input("Enter your name: ")  # Taking input from the user
print("Hello, " + s + "!")  # Displaying the input received from the user
print(type(s))  # Type of the input received from the user
# Try It Yourself 
''' 2-7 
Store a person’s name, and include some whitespace 
characters at the beginning and end of the name. Make sure you use each 
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, 
lstrip(), rstrip(), and strip()
'''

#Solution 
myName = "\t  Faizan Ahmad \n  "
print(myName)
print(myName.lstrip())
print(myName.rstrip())
print(myName.strip())


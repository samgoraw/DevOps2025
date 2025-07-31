str1 = "Hello"
str2 = "World"
str3 = '''
       This is my multiline string

       '''
greeting = str1 + " " + str2
print(greeting)
print(str3)
print(f"{str1} {str2}")
print((str1 + " ") * 3)
print(str1[0])
print(str1[-1])

# Slicing String
print(str1[0:3])#Hel
print(str1[2:])#ll0

# Slicing length
print('Length of Str1:',len(str1))

# Changing Case
print('Upper Case:', str1.upper())
print('Lower Case:', str1.lower())

## Searching
print("lo" in str1)
print(str1.find("lo"))

## Replace
new_str = str1.replace("H","W")
print(new_str)

## Split and Join
statement = "My name is Sam and I am a DevOps Engg."
words = statement.split()
print(words)
print("-".join(words))

#Striping Whitespaces
print("  hello    ".strip())

## Checking with Start and End value
print("Python".startswith("Py"))
print("Python".endswith("on"))





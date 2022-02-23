#Multi line string with three double quotes
var_string_3 = """THREE DOUBLE QUOTES MULTI LINE STRING: Welcome to python 
tutorials by tinitiate.com,This is a multi line string
as you can see"""

print(var_string_3)

#Splitlines(), Converts multi-line strings to a list
testString = """Line 1
Line 2
Line 3
"""
print(testString.splitlines())

###Work with portions of string
##find()/index(): displays the position index of a given substring and its occurence number

print('test'.find('t',2))
print('test'.index('t'))
print('test'.find('z'))
print('test'.rfind('z')) #rfind() prints the highest index and -1 when not found
print('test'.rfind('t'))

#replace
print('test'.replace('t','r'))

#split
print('This is a test'.split()) # prints a LIST, seperated by a whitespace
print('This|is|a|test'.split('|')) # prints a LIST,  seperated by a pipe |
print('This,is,a,test'.split(',')) # prints a LIST,  seperated by a comma ,

##String as arrays
var_test_string = "Python is cool"
print(var_test_string[0]) #First character of the string is [0]
print(var_test_string[-1]) #Last character of the string is [-1]
print(var_test_string[-4]) #Fourth character of the string from the end

##Slicing strings
var_test_string = "Python is cool"
print(var_test_string[6:])
print(var_test_string[-4:])
print(var_test_string[4:10])

##Removing parts of a string
print('    This is a test'.strip())
print('This is a test '.strip('t')) #removes the last occurence of 't'
print('This is a test '.lstrip('This')) #removes the last occurence of 'This'

##String alignment justify
print('test'.ljust(10,'+'))
print('test'.rjust(10,'+'))
print('test'.center(10,'+'))




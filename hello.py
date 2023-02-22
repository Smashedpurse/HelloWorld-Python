#Hello World, this is a comment.
#Hi everyone, this is a second comment.
print("Hola Python")
print('Hello World')
"""
This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
'''
This is another comment multiline
:D
'''

#List - Arrays
constList= [1,2,3]
print(constList)

differentInfo = ['Bannana',10,False,0.81]
print(differentInfo)

#Dictionary - Object
ProfileResume={
    'first_name':'Ivan',
    'second_name':'Rubio',
    'country':'Mexico',
    'age':23,
    'is_married':False,
    'skills':['JS','React','Node','Python']
}
print(ProfileResume)

#Tuple - A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

myFirstTuple = ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
print(myFirstTuple)

('Earth','Jupiter','Venus','Mars') #Planets

#Set A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.
myFirstSet = {3,23,23,5,75.2}
print(myFirstSet)


#Checking Data types
#To check the data type of certain data/variable we use the type function. In the following terminal you will see different python data types:

print(type(myFirstSet)) #Set
print(type(myFirstTuple))#Tuple
print(type(ProfileResume))#Dictionary
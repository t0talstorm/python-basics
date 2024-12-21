#typecasting = the process of converting the data type of a value to another data type
# str() , int() , float() , bool()
#useful when you want to perform operations on variables of different data types
#useful for user input

name = "Jhon doe"
age = 25
gpa = 3.2
is_student = True

gpa =int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name =bool(name) #gives false if the string is empty
print(name)
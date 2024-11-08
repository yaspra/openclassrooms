# This script is created to aid the 
# practices and exercises in 'learn Python Basics course".
# Exercise 1 , using print function 
#   to save in program and run the prog from terminal.
print("I learn Python")
print(17 + 35 * 2)

#exercise 2. - learing to declare a variable and 
#modifying value of the variable.
age = 40
name = "pvaddadi"
height = "175 cms"
is_student = "python course"
print("my name is",name,"and am",age,"years old." "I am currently in",is_student,"","classroom")

print("variables used in above statement have below types")
print("name =",type(name))
print("age =" ,type(age))
print("height =" ,type(height))
print("is_student =" ,type(is_student))
# below exercise is for lists and list method
fruits =["apple","banana","orange"]
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.append("pineapple")
fruits.sort
print(fruits)

# below is the module exercises for program flow
sunny = False
if sunny:
    print("go to the beach!")
else:
    print("stay inside!")
    
 # below HW for program flow
left_number =23
right_number=3
symbol = ['+','-','*','/']
result = 0
print(type(left_number))
print(type(right_number))
if type(left_number) == int and type(right_number) == int: print("yes they are integers")
elif type(left_number) != int and type(right_number) != int:print("useless")
elif type(left_number) != int or type(right_number) != int:print("not ints")

match(symbol):
    case"+": result = left_number + right_number
    case"-":result = left_number - right_number
    case"*":result = left_number * right_number
    case"/":result = left_number /right_number 
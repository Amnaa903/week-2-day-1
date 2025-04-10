#functions without parameters
#create or define a function
def greet():
    print("Hello, welcome to Python programming!")
#call or invoke a function
greet()
#functions with parameters
def add2numbers(num1, num2):
    return num1 + num2
#call or invoke a function
result = add2numbers(10, 20)
print("The sum is:", result)
#functions with return statement
def multiply(num1, num2):
    return num1 * num2
#call or invoke a function
result = multiply(10, 20)
print("The product is:", result)
#convert farenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
#call or invoke a function
fahrenheit = 100
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
#convert celsius to farenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
#call or invoke a function
celsius = 37.5
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
#Multiple inheritance
class Parent1:
    def method1(self):
        print("Method from Parent1")
class Parent2:
    def method2(self):
        print("Method from Parent2")
class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")
#Creating an object of the Child class
child_object = Child()
#Calling methods from Parent1 and Parent2 using the Child object
child_object.method1()
child_object.method2()
#Calling method from Child class
child_object.method3()
#Single inheritance
class Parent:
    def method1(self):
        print("Method from Parent")
class Child(Parent):
    def method2(self):
        print("Method from Child")
#Creating an object of the Child class
child_object = Child()
#Calling method from Parent class using the Child object
child_object.method1()
#Calling method from Child class
child_object.method2()
#constructor
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
#Creating an object of the Person class
person1 = Person("Alice", 30)
#Calling the display_info method
person1.display_info()
#calling super method
class Parent:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"Name: {self.name}")
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the constructor of the Parent class
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
#Creating an object of the Child class
child_object = Child("Bob", 25)
#Calling the display_info method
child_object.display_info()
#Calling the display_name method from Parent class
child_object.display_name()
#Creating a list
my_list = [1, 2, 3, 4, 5]
#Adding elements to the list
my_list.append(6)
my_list.append(7)
# duck typing
class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I can quack too!")
#Function that accepts any object with a quack method
def make_it_quack(duck):
    duck.quack()
#Creating objects of Duck and Person classes
duck = Duck()
person = Person()
#Calling the function with both objects
make_it_quack(duck)   # Output: Quack!
make_it_quack(person) # Output: I can quack too! 

numbers = [2, 4, 6, 8, 10]
result = list(map(lambda x: x * 7, numbers))
print(result)


words = ["sky", "tree", "azzzzzz","brrr", "cloud", "myth", "sun"]
vowel_words = list(filter(lambda word: any(char in 'aeiouAEIOU' for char in word), words))
print(vowel_words) 
from functools import reduce
numbers = [2,2,1,1,2,20]
# Multiply all numbers using reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)
# Sum all numbers using reduce
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)
# Find the maximum number using reduce
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
# Find the minimum number using reduce
min_number = reduce(lambda x, y: x if x < y else y, numbers)
print(min_number)
# Find the average using reduce
average = reduce(lambda x, y: x + y, numbers) / len(numbers)
print(average)
# Find the median using reduce
sorted_numbers = sorted(numbers)
if len(sorted_numbers) % 2 == 0:
    median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
else:
    median = sorted_numbers[len(sorted_numbers) // 2]
print(median)
#operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
#Creating two vector objects
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
#Adding the two vectors
result_add = vector1 + vector2
print("Addition:", result_add)  # Output: Vector(6, 8)









#file handling
#open a file in write mode
file = open("example.txt", "w")
#write to the file
file.write("Hello, this is a test file.\n")
file.write("This is the second line.\n")
#close the file
file.close()
#open a file in read mode
file = open("example.txt", "r")
#read the contents of the file
contents = file.read()
#display the contents
print("File Contents:")
print(contents)
#close the file
file.close()
#open a file in append mode
file = open("example.txt", "a")
#append to the file
file.write("This is an appended line.\n")
#close the file
file.close()
#open a file in read mode
file = open("example.txt", "r")
#read the contents of the file
contents = file.read()
#display the contents
print("Updated File Contents:")
print(contents)
#close the file
file.close()

# exception handling
try:
    #code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    #handling the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    #handling any other exception
    print("An error occurred:", str(e))
finally:
    #this block will always execute
    print("Execution completed.")
#using try except with else block
try:
    #code that may raise an exception
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    #handling the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    #handling any other exception
    print("An error occurred:", str(e))
else:
    #this block will execute if no exception occurs
    print("Result:", result)
finally:
    #this block will always execute
    print("Execution completed.")
#using try except with finally block
try:
    #code that may raise an exception
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    #handling the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    #handling any other exception
    print("An error occurred:", str(e))
else:
    #this block will execute if no exception occurs
    print("Result:", result)
finally:
    #this block will always execute
    print("Execution completed.")
#using try except with finally block
try:
    #code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    #handling the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    #handling any other exception
    print("An error occurred:", str(e))
else:
    #this block will execute if no exception occurs
    print("Result:", result)
finally:
    #this block will always execute
    print("Execution completed.")

# Map 












###exercise example 1
numbers3 = [5, 2, 3, 5, 2, 9, 6, 9, 6, 10]
print("The original list is: " + str(numbers3))
###using set()
numbers3 = list(set(numbers3))
print("The list after removing duplicates: " + str(numbers3))   ###this method will give results ascendingly
##example 2 to remove duplicates
numbers3 = [5, 2, 3, 5, 2, 9, 6, 9, 6, 10]
uniques = []
for num in numbers3:
    if num not in uniques:
        uniques.append(num)
print(uniques)

#####Tuples
##Tuples are like list. we can store list of values, names etc but we cannot modify to addy any new ones
###In tuples, we define list using () but in list we use []. this is a difference b/w them
###we can only use count() - to count the no. of items and index() - to find the index of an item
number = (5,1,2)
print(number.index(5))  ##to get the index of this value
print(number[0])   ###to get the first index value
####Unpacking####
###this is a method that will unpack the values from the Tuple and also from list values
###for eg:
coordinates = (1, 5, 6) ###tuple variables
x, y, z = coordinates  ###python will automatically assign the tuple values to x, y, z - x = 1, y = 5, z = 6
##this is called unpacking
print(x) ###you will get x value i.e.,1
##also applicable for list values
number_list = [6,9,10]
x,y,z = number_list
print(z)

###Dictionaries###
##It is a structure that allows us to map a key to a value
##example
patient = {
    "name": "Pinky",
    "age": 22,
     "is_verified": True
}
patient["birth_date"] = "July 19, 1998" ###to add values in dictionaries
patient["name"] = "Raagul" ##to change the name or any values
##if we ask for some other values which is not in the dictionary the python will yell at us.
###To not any errors, use get()
print(patient.get("weight")) ##this value is not in patient, but the python will not show any error. instead it shows
###None - python returns None when there is no value
###we can also use get() to add values in dictionary
print(patient.get("weight", "65kgs"))  ##you will get 65kgs

##exercise using dictionary
phone = input('Phone number: ')
number_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "five",
    "6":  "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for chr in phone:
    output += number_mapping.get(chr, "!") + " " ##we are using get(), in case the user enters some other value, the program doesn't yell at them, it returns !
###and we added space to have spaces b/w each values
print(output)

##emoji converter using dictionary
###In this function, we use split() to split the words from the user (the spacing)
msg = input(">")
words = msg.split(' ') ###the mention of space here is - it will separate as list
####print(words) ##if the user writes, john smith - it returns ['John', 'smith']
emoji = {
    ":)": "😀",
    ":(": "☹"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
###using get(), we are getting user word to match the emojis, if it is not applicable, it will return the same word
print(output)

####Functions###

###define (def) function
##example
def greet_user():
    print("Hello!!🦹‍♀")
    print("Welcome! to insane asylum 📢")


###always leave 2 line space after using def function
print("Beginning")
greet_user()
print("End!")

###Parameters#####
###how to pass user info in functions##
def greet_user(first_name, last_name):  ###we are passing parameters to this function - name
    print(f"Hello!! {first_name} {last_name} 🦹‍♀")
    print("Welcome! to insane asylum 📢")


###always leave 2 line space after using def function
print("Beginning")
greet_user("Pinky", "Raagul")
greet_user("Stella", "Johnson")  ###we can use this function to pass many names as we want - this is the use of this function
greet_user(last_name="Johnson", first_name= "Stella")  ###this the keyword arugument. with this the positions of arguments doesn't matter
print("End!")
##always add a position argument first and then keyword arguments, if you are using both

###Return statement#####
###calculating square of a value using square()

def square(number):
    return number * number


result = square(9)
print(f"The square is: {result}")
###or
print(square(9))

###Exercise - using the emoji coverter code in a def function
def emoji_changer(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_changer(message))

####Exceptions###
###How to handle errors in a program...and to get proper error msg without the program yelling at the user

try:
    age = int(input('Age: '))
    income = 50000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0!") ###if the user types age as 0
except ValueError:
    print("Invalid value")   ###this is how you avoid program crashing

####Classes###
###we use classes to define new type to model the real concepts
###in class, the first letter of name must be defined in caps and connective words too - eg PointBreaker
####
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.draw()  ##this will print draw

point2 = Point()
point2.x = 1
print(point2.x)
point2.move()

####Constructors####

class Point:
    def __init__(self, x, y):   ###this is used to construct new objects to the class __init__ is initialize
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(20, 30)
###we can also change the x or y value
point.x = 23
print(point.x)   ###this will print 23 as o/p

##exercise

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I'am {self.name}")


pinky = Person("Pinky Raagul")
print(pinky.name)
pinky.talk()
raagul = Person("Raagul Pinky")
raagul.talk()  ###you can type different as many times as you want because the function is defined

##Inheritance###
###dont repeat youserself (Dry) - in python dont repeat your code
###in class, if you want to use same method for diff class, dont repeat the code instead use a parent class
##From parent class, the rest of the class can inherit the information

##example
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  ##add your parent class name in the attributes ###pass doesn't mean anything.. it says to python ...just pass the line there is no problem ###Because you can't leave a empty class
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


#####now you can access both the classes
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()


####Modules####
###To better organise our code, we can break the codes in different files instead of saving in one .py file
###That is called modules. It also have the ability to reuse our code

###save your code in a new file and import them in this file Lists.py
###I have created another file called "converter.py" and wrote a code def code for weight converters
###Import the file using "import file_name (no extension"

import converter

print(converter.kgs_to_lbs(65))   ###when you type converter you will get the def functions

from converter import kgs_to_lbs  ###another way to import the specific function u want to use
#####after the import in line 250 press ctrl + space, then you will get your functions
###instead of typing converter.kgs_to_lbs, you can write as follows
kgs_to_lbs(100)

###exercise:

###creating a module to create the max value from a list
###utils module file is created

from utils import find_max

numbers = [10, 52, 69, 85, 66]
maximum = find_max(numbers)
print(maximum)

####Package####
###Package is used to store a bunch of modules. In file system terms, a package is a directory or folder
###to create a package right click the project -> new -> directory
###and again create a .py file with __init__ name and delete that directory
###Now create a python package from your project name
###now u will automatically get the __init__.py file with your package
###I have created a shipping.py module inside this package
##to access this package use import package_name.modulename

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

##or
from ecommerce.shipping import calc_shipping
calc_shipping()
###this is how you access the functions in package

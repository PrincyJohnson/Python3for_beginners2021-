print("Josephine Princy Johnson")
print('o^---')
print(' ||||')
print('*' * 10)

##############################
##Assigning 3 variables
full_name = 'Pinky'
age = 22
is_new = True

###############################
###Asking inputs from the user###
name = input('What is your name? ')
print("Hi " + name)

####exercise
new_name = input('What is your name? ')
colour = input('What is your favourite colour? ')
print(new_name + " likes " + colour)

#####################Calculating the age using birth year#########################
birth_year = input('What is your birth year? ')
##type() function tells you the class of variables###
print(type(birth_year))
###why? int(birth_year) means the above value is in string. we cannot subtract integer with string. convert the str using int() and subtact it####
age = 2021 - int(birth_year)
print(type(age))
print(age)

#########exercise
weight = input('What is your weight in pounds? ')
#########we can use either int() or float() to multiply the pounds with decimals(kgs)##########
kgs = int(weight) * 0.453592
print(weight, " pounds are equal to ", kgs, ' in kilograms ')

#############printing an email using 3 quotes'''###################
email = '''Hi Mama,
I miss you baby,
I need you to be with me every day, every minute and every second.
Love,
Pinky 
'''
print(email)

######indexes###
course = 'Python for beginners'
##########012345            -2-1##############
print(course[0])  ####prints P
print(course[0:5]) ###prints Pytho - from 0 to 4 --it will not print 5th index (overall is 5 digits)#############
print(course[:])  ###prints entire o/p -- it assumes 0:-1 that means the entire o/p #############
####or
another = course[:]
print(another)  ###another is the replica for course... it will print the entire o/p#####

###formatted stings##################
first = 'Pinky'
last = 'Raagul'
message = first + ' [' + last + '] is a coder'  ####this is usal string concatenation format###
print(message)
####other way called formatted string using f####
msg = f'{first} [{last}] is a coder'
print(msg)

######string methods####
course = 'Python for beginners'
print(len(course)) ####it will print the length of course --- this is not string methonds, this is just an another function###

print(course.upper())  ####this will print the course value in upper case -- .lower() for lower case###
print(course.find('P')) ###this will return the index of P in course value####
print(course.replace('Beginners', 'Absolute beginners')) ###replacing the words in course
print('Python' in course)  ####detecting the Python name in course using  in operator boolean which returns true/false###
print(course.title())  ###prints the title

####Arithmetic operators###
print(10 + 3)  ##addition
print(10 - 3)  ##subtraction
print(10 * 3)  ##multiply
print(10 / 3)  ##division which will return the values in floating decimal
print(10 // 3)  ##division which will return the value in integer
print(10 % 3)  ##modulus will return the remainder in the division
print(10 ** 3)  ##exponent will return 10^3 value which is 1000
###incrementing
x = 10
x = x + 3
##or
x += 3 ###enhanced printing option the above line and this line are same
x -= 3
print(x)

###Operator precedence###
####order of operations
###paranthesis gives priority to any operator
##1. exponentiation **
###2. multiply or division
###3. addition or sub
x = 10 + 3 * 2  ###first * is done and addition
print(x)

####Math functions###
x = 3.9
###to round this value, use built-in round() function
print(round(x))
###another built-in func is "abs" which is absolute function which returns only +ve value from the data
x = -3.9
print(abs(x))  ##o/p is 3.9

####we can import math function and use diff func in it
import math

print(math.ceil(x))  ###this will return the round value of x
print(math.floor(x))  ###this will return the first value eg x = 2.9 returns 2
###visit web page called python 3 math functions for more ####

####If statements###
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Dink plenty of water")
elif is_cold:
    print("It's a cold weather")
    print("Wear warm cloths")
else:
    print("It's a lovely day")
print("Have a great day")

##exercise
price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
    print("The buyer needs to put down 10%")
else:
    down_payment = 0.2 * price
    print("The buyer needs to put down 20%")
print(f"The down payment is ${down_payment}")

#####logical operators#####
###such as AND OR  NOT operators

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
###or we can use or operator to see atleast one value is true
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

###AND = both variable true
##OR = atleast 1 is true
##NOT = It coverts the boolean variable if its true then converts to false

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:   ###not converts the boolean of criminal record to true
    print("Eligible for loan")

####Comparison operators
### <, >, <=, >=, ==###########
temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
###exercise
name = input("What is you name? ")
print(len(name))

if len(name) < 3:
    print("Name must be atleast 3 chr long")
elif len(name) > 50:
    print("Name can be max of 50 chr long")
else:
    print("Name looks good")
print(f"The Name is {name}")

####weight converter

weight = int(input("Weight: "))
unit = input("(L)lbs or (K)kgs: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos")
elif unit.upper() == "K":
    converted = weight // 0.45
    print(f"Your weight is {converted} pounds")
else:
    print("Error")

#####While loops####
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

#####
i = 1
while i <= 5:
    print('*' * i)  ###this is produce i times of * for each loop
    i += 1
print("Done")

###guessing game###

secret = 12
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret:
        print('You won!')
        break
else:
    print("Oops! you failed")

####Car game
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started.... Ready to go....")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped..")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        
        """)
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand that")


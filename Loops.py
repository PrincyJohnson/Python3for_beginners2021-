#####For loops####

#####examples

for item in 'Python':  #####for loops -- item variable will hold one chr at a time in each iteration
    print(item)
for item in ['Red','Orange','Blue']:  ###we can do this also with numbers [1,2,3,4,]
    print(item)
#####range function
for item in range(10):
    print(item)  ###prints from 0 to 9
for item in range(5,10):
    print(item)   ###prints from 5 to 9
for item in range(5,10,2):
    print(item)   ###prints values from 5 , 5+2=7, 7+2 = 9
####exercise
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

####Nested loops####3
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
##exercise
numbers = [1,1,1,5]
#####for num in numbers:
#####print('x' * num)   ####simple format
###another format
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#####list#######
names = ['Raagul','Pinky','George','elena']
names[1] = 'Princy'  ###to change the names
print(names[1])

numbers = [1,2,5,9,12,6]  ###to get which number is greater
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

###2D lists######
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][0])
for row in matrix:
    for item in row:
        print(item)

####List methods#####
##to add a values at the end of the list use 'append'
numbers = [5,2,1,2,3,8]
numbers.append(20)  ###to add at the end
print(numbers)
numbers.insert(0,6)  ###to add in between or in the beginning of a list use insert(index, value)
###to remove a value from a list
numbers.remove(5)
###to clear the entire list
numbers.clear()  ###it empties the list
###to remove the last item in the list
numbers = [5, 1, 6, 9, 10]
numbers.pop() ##without mentioning any value it will automatically remove the last value from the list
print(numbers)
###to find the index of values
numbers = [5, 1, 6, 9, 10]
print(numbers.index(2))  ###it will find the index of value 2
###we can also check the existence of a number or characters
numbers = [5, 1, 6, 9, 10]
print(50 in numbers)  ###using in operator we can find the values in a string...this will return boolean value -false
###to count the repeated numbers in a list use count(value)
numbers = [5, 1, 6, 9, 10]
print(numbers.count(2))  ##this will return the no of 2 in the list
###to sort our list in ascending orders
numbers = [5, 1, 6, 9, 10]
numbers.sort() ###sort() does not takes any value ...it places the list in ascending order
print(numbers)
###to sort the list in descending order - 1st sort the list and use reverse() function to reverse it
numbers = [5, 1, 6, 9, 10]
numbers.sort()
numbers.reverse()
print(numbers)
###to copy a list to another list
numbers = [5, 1, 6, 9, 10]
numbers2 = numbers.copy()  ###this is a copy of the original cumbers list.
###if any changes happens in the numbers list it will not change the numbers2 list. they are both independent list
numbers.append(10)  ###this will add 10 to numbers list at the end but this will not change the number2 list.
print(numbers2)
###exercise example 1
numbers3 = [5, 2, 3, 5, 2, 9, 6, 9, 6, 10]
print("The original list is: " + str(numbers3))
###using set()
numbers3 = list(set(numbers3))
print("The list after removing duplicates: " + str(numbers3))
##example 2 to remove duplicates
numbers3 = [5, 2, 3, 5, 2, 9, 6, 9, 6, 10]
uniques = []
for num in numbers3:
    if num not in uniques:
        uniques.append(num)
print(uniques)
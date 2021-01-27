
# initializing an empty list
mylist = []


# initializing a list with the values of 1, 2, 3 in it
mylist = [1, 2, 3]


# checking the length of the list
print(len(mylist))


# appending an element to the end of the list
mylist.append(4)
print(mylist)


# removing an element from the list with value 2
mylist.remove(2)
print(mylist)


# removing an element from the list at index 0
del mylist[0]
print(mylist)


# popping a value from the list into a variable
myvar = mylist.pop(0)
print(myvar)
print(mylist)


# assigning 3 to the index 0 of the list
mylist[0] = 3
print(mylist)


# Example of a method that takes in a number and displays even numbers
def calcEvens(num):
  evens = []
  for i in range(num):
    if i % 2 == 0:
      evens. append(i)
  print(evens)


# This is an example of a method call
calcEvens(10)


# Example of list comprehension to display even numbers
print([i for i in range(10) if i % 2 == 0])


# list comprehension to iterate through 2 lists and print each element together
# this uses the zip function 
names = ['Bryan', 'Hayley']
ages = [35, 36]
person = [(i, j) for i, j in zip(names, ages)]
print(person)

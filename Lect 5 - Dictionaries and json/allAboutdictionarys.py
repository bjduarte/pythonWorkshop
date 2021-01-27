
import sys
import os
import io
import json

# creating a dictionary with my info
myDict = {"name": "Bryan", "age": 33, "gender": "male"}
print("My Dictionary")
print(myDict)


# removing the key and value, "name"
nameToRemove = myDict['name']
del(myDict["name"])
print(nameToRemove, 'has been removed!')
print(myDict)


# creating a list with mentor names
mentorNameList = ["Amanda", "Bryan", "Kinsey", "Maureen"]

# creating a list with student names
studentNameList = ["Ashley", "Bob", "Claire", "Dave", "Elaine", "Frank", "Grace", "Homer"]

# creating a dictionary with the above lists as values
workshopDict = {"Mentor Names": mentorNameList, "Student Names": studentNameList}
print('Workshop Dictionary has been created!')
print(workshopDict)

# adding a new key and value list called ages
workshopDict["ages"] = [20, 21, 22, 23, 24, 25, 26, 27, 28]
print('Ages have been added to dictionary')
print(workshopDict)


# printing only the mentor names from the dictionary
print('Mentors are: ')
print(workshopDict["Mentor Names"])


# printing only the student names from the dictionary
print('Students are: ')
print(workshopDict["Student Names"])


# printing only the ages from the dictionary
print('Ages are: ')
print(workshopDict["ages"])


# printing only the first mentor name from the list in the dictionary
print('The first mentor is: ', workshopDict["Mentor Names"][0])
# printing only the second student name from the list in the dictionary
print('The second student is: ', workshopDict["Student Names"][1])
# printing only the third age from the list in the dictionary
print('The third age is: ', workshopDict["ages"][2])
# printing all 3 on one line
print('The second mentor, first student, and third age')
print(workshopDict["Mentor Names"][1], workshopDict['Student Names'][0], workshopDict['ages'][3])


# setting an item from the list to a local variable
myName = workshopDict["Mentor Names"][1]
print("My name is:", myName)


# changing my name in the list in the dictionary
workshopDict["Mentor Names"][1] = "Bryan Duarte"
myFullName = workshopDict["Mentor Names"][1]
print("My full name is:", myFullName)


# Writing a dictionary to json
print('Writing the dictionary to a json file named testFile.json')
pathToFile = './Desktop/workshopFiles/testFile.json'
with open(pathToFile, 'w') as fout:
  json.dump(workshopDict, fout)
  fout.close()
  print('Data has been written')


# reading in a json file into a dictionary
print('Reading in testFile.json back into a dictionary')
with open(pathToFile) as fin:
  data = json.load(fin)
  for p in data:
    print('Mentor Names: ', data['Mentor Names'])
    print('Student Names: ', data['Student Names'])
    print('Ages: ', data['ages'])


# printing two of the dictionaries key value pairs together
print([(i, j) for i, j in zip(data['Student Names'], data['ages'])])


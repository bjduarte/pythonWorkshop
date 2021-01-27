
# The topics to cover
'''
Classes
Methods
Constructors
Self
scope
Parameter lists
Getters
Setters
'''

# class declaration
# class is a key word
# the colon is after the class name
# no parens necessary

class Person:
  #global varible

# class constructor 
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    self.age = 0

#  self 
# self is used to represent an instance of the class known as a member of the class. 
# self allows for attributes or methods of the class to be referenced
# It binds the attributes with the given arguments. 
# Python does not use the ‘@’ syntax to refer to instance attributes. 
# self is also used to refer to a variable field within the class. 


  def showPerson(self):
    print(self.name, " is a ", self.gender)


  def getAge(self):
    return self.age


  def setAge(self, age):
    self.age = age


def main():
  person1 = Person('Bryan', 'male')
  person2 = Person('Hayley', 'female')
  person1.showPerson()
  person2.showPerson()

  person1.setAge(50)
  personAge = person1.getAge()
  print(personAge)


if __name__ == '__main__':
  main()
  
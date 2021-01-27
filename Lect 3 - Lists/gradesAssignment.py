
# This program should do the following
# the first method should add students to a list of strings
# the second method should compute the grades for 5 assignments
# the third method should print the student along with their average grade over all assignments on the same line.

studentName = []
grade = []
assignments = ["Assignment1", "Assignment2", "Assignment3", "Assignment4", "Assignment5"]


def addStudent():
  """For this method you need to add all new students to the studentName list. I took care of the line to read the input."""
  newStudent = input("Enter students name: ")

  pass


def computeGrade():
  """For this method I want you to calculate the grade of the students for each assignment and add the final grade to the grade list. I took care of the input."""

  for i in assignments:
    assignmentGrade = input("Enter the grade for " + i)

  pass


def printGrades():
  """In this method I want you to print each students name and their final grade on the same line."""
  print("No grades have been computed yet!")


def main():
  classSize = 3
  numOfStudents = 0
  while numOfStudents < classSize:
    addStudent()
    computeGrade()
    numOfStudents+=1

  printGrades()

if __name__ == '__main__':
  main()

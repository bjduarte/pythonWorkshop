# write a method signature here that is called count_while_counting
# the method should take in 2 parameters
# param1: starting_point, param2: ending_point
# this method should use a loop to count from your starting point to your entding point
# if I pass in 1 and 10 it should print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# This method does not have to return any values
def count_while_counting(starting_point, ending_point):
  

  pass

# Write a method signature here called compute_my_grade
# This method should take in 1 parameter
# param1: my_grade
# This method should take in my_grade and determin my letter grade
# Grade scale: 90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, 59 and lower = F
# This method should return a single letter based on the number passed in
# Note, floating point numbers for the my_grade variable is not necessary integers are fine
def compute_my_grade(my_grade):
  # Delete this line and # insert your code here
  pass


# Do not touch code below this point!!!
# This is how I am testing your program
def main():
  print("Test 1: Testing inputs 1, 10")
  print("Expected output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
  print("Your output: ")
  count_while_counting(1, 10)

  print("Test 2: Testing inputs 50, 60")
  print("Expected output: 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60")
  print("Your output: ")
  count_while_counting(50, 60)

  print("Test 3: Testing input 90")
  print("Expected output: Your grade is: A")
  print("Your output: ")
  test3 = compute_my_grade(90)
  print("Your grade is: " + str(test3))

  print("Test 4: Testing input 82")
  print("Expected output: Your grade is: B")
  print("Your output: ")
  test4 = compute_my_grade(82)
  print("Your grade is: " + str(test4))

  print("Test 5: Testing input 65")
  print("Expected output: Your grade is: D")
  print("Your output: ")
  test5 = compute_my_grade(65)
  print("Your grade is: " + str(test5))
  
if __name__ == "__main__":
  main()
  
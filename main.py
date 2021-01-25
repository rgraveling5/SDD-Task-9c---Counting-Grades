"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""
names = []
grades = []
    
for x in range(2):
  names.append(input("Name: "))
  grades.append(input("Grade: "))

for x in range(len(grades)):
  total = 0
  print()
  search = input("Grade to search for: ")
  for x in range(0, len(grades)):
      if search == grades[x]:
          total = total + 1
  print("The grade " + str(search) + " was found " + str(total) + " time(s)")
  print()



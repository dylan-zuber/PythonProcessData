"""
	Name: Dylan Zuber
	Assignment: PA 4
	Course/Semester: CS343/Fall2020
	Lab Section: N/A
	Sources Consulted: https://careerkarma.com/blog/python-sort-a-dictionary-by-value/

  Description: program reads a text file containing names followed by 12 digits, the first digit representing number of times a name is seen in 1900 and the 12 digit representing the number of times the same name is seen in 2010. The program allows a user to be given a list of all names and their most popular year when the user inputs a string, the user can input a specific name and every year for that speficic name will be displayed, and a user can input a year and will be presented with the top 10 names (10 boy names, 10 girl names) for that year from most votes to the people with the 10th most votes.
"""
# To hold all data read from file (keys being names and values are arrays of length 12, index 0 representing 1900 and index 11 representing 2010)
database = {}

file = "input.txt"
firstLine = 0
size = 0

#reads file and populates database dict
with open(file) as f:
  for line in f:
    if firstLine == 0:
      size = line
    i = 0
    years = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    name = ""
    for word in line.split():
      if i == 0:
        name = word
      else:
        years[i-1] = int(word)
      i = i + 1
    database[name] = years
f.close()

"""
Given a name, displays all names that contain the "name" substring and their most popular year
@param name user input, substring to check all names in database
"""
def search(name):
  listNames = []
  name = name.lower()
  for key in database:
    keyCompare = key.lower()
    if name in keyCompare:
      arr = database.get(key)
      max = 0
      year = 1900
      maxYear = year
      for i in arr:
        if i > max:
          max = i
          maxYear = year
        year += 10
      addName = key + " " + str(maxYear)
      listNames.append(addName)

  if len(listNames) == 0:
    print("no names matching input :-()")
  for name in listNames:
    print(name)


"""
Given a string, the user will be displayed with all of the information stored on that exact name
@param exactName string input by the user that is expected to match a name in the database exactly
"""
def exactNameSearch(exactName):
  if exactName in database:
    print("Rankings for \"", exactName,"\":")
    i = 1900
    for val in database.get(exactName):
      print(i, ": ", val, ", ", end = '')
      i += 10
    print("")
  else:
    print("name not in database :-(")


"""
Given a year between 1900 and 2010 (has to be the start of a decade), the top ten boy and girl names will be displayed
@param year year input by the user between 1900 and 2010, has to be the beginning of a decade
"""
def popularNameByYear(year):
  listYear = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
  if year in listYear:
    i = 0
    while(year != 1900):
      i += 1
      year -= 10
    print(i)
    namesPerYear = {}
    for key in database:
      arr = database.get(key)
      namesPerYear[key] = arr[i]  
  
    #Source
    sortedNamesPerYear = sorted(namesPerYear.items(), key=lambda x: x[1], reverse=True)
    i = 0
    j = 1
    while i < 20:
      first = sortedNamesPerYear[i]
      i += 1
      second = sortedNamesPerYear[i]
      print(j, ". ", first[0], ", ", second[0])
      i += 1
      j += 1
  else:
    print("make sure your input is on the decade between 1900 and 2010 ( ͡° ͜ʖ ͡°)")


run = True

while run:
  print("PA 4 - Name database")
  print("--------------------")
  print("(1)  Search  (2)  Popularity over time  (3) Top Ten  (4)  Quit")

  userInput = input("Enter choice: ")
  if userInput == "1":
    searchName = input("Enter name: ")
    search(searchName)
    run = True
  elif userInput == "2":
    exactName = input("Enter EXACT name: ")
    exactNameSearch(exactName)
  elif userInput == "3":
    searchYear = input("Enter year: ")
    popularNameByYear(int(searchYear))
    run = True
  elif userInput == "4":
    print("thank you everyone for coming ✌(ツ)")
    run = False
  else:
    print("gosh darn it! that isn't 1, 2, 3 or 4 :P")
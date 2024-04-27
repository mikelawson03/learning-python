import os, time

nameList = []

while True:
  os.system("clear")
  print("Please enter first name:")
  fName = input(">>").strip()
  print("Please enter last name:")
  lName = input(">>").strip()
  fullName = (f"{fName} {lName}").title()
  if fullName not in nameList:
    nameList.append(fullName)
  print("Adding name...")
  time.sleep(0.75)
  os.system("clear")
  print("THIS IS EVERYONE I KNOW:")
  print("-------------------------")
  for name in nameList:
    print(name)
  while True:
    print("\nWould you like to add more names?")
    choice = input(">>").strip().lower()
    if choice in ("y", "yes"):
      break
    elif choice in ("n", "no"):
      exit()
    else:
      print("I don't recognize that. Please try again.")
      
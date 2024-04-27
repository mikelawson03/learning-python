import random, math, time, os, string

#dict containining classes, their starting HPs, and their descriptions
classInfo = { 
    'barbarian': { 
        'startingHp': 12, 
        'description': 'A fierce warrior who can enter a battle rage',
        'primary' : 'Strength'
    },
    'bard': {
        'startingHp': 8, 
        'description': 'An inspiring magician whose power echoes the music of creation',
        'primary' : 'Charisma'
    },
    'cleric': {
        'startingHp': 8, 
        'description': 'A priestly champion who wields divine magic in service of a higher power',
        'primary' : 'Wisdom'
    },
    'druid': {
        'startingHp': 8, 
        'description': 'A priest of the Old Faith, wielding the powers of nature and adopting animal forms',
        'primary' : 'Wisdom'
    },
    'fighter': {
        'startingHp': 10, 
        'description': 'A master of martial combat, skilled with a variety of weapons and armor',
        'primary' : 'Strength or Dexterity'
    },
    'monk': {
        'startingHp': 8, 
        'description': 'A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection',
        'primary' : 'Dexterity & Wisdom'
    },
    'paladin': {
        'startingHp': 10, 
        'description': 'A holy warrior bound to a sacred oath',
        'primary' : 'Strength & Charisma'
    },
    'ranger': {
        'startingHp': 10, 
        'description': 'A warrior who combats threats on the edges of civilization',
        'primary' : 'Dexterity & Wisdom'
    },
    'rogue': {
        'startingHp': 8, 
        'description': 'A scoundrel who uses stealth and trickery to overcome obstacles and enemies',
        'primary' : 'Dexterity'
    },
    'sorceror': {
        'startingHp': 6, 
        'description': 'A spellcaster who draws on inherent magic from a gift or bloodline',
        'primary' : 'Charisma'
    },
    'warlock': {
        'startingHp': 8, 
        'description': 'A wielder of magic that is derived from a bargian with an extraplanar entity',
        'primary' : 'Charisma'
    },
    'wizard': {
        'startingHp': 6, 
        'description': 'A scholarly magic-user capable of manipulating the structures of reality',
        'primary' : 'Intelligence'
    }
  }
classList = [x for x in classInfo.keys()]
allLetters = string.ascii_lowercase


def statRolls():
    statRolls = []
    #Generate 4 rolls
    for i in range(1,5): 
        statRolls.append(rollDice(6))
    #Drop lowest roll
    lowestRoll = min(statRolls) 
    statRolls.remove(lowestRoll)
    #Add rolls together  
    stat = sum(statRolls)
    #Calculate modifier and generate string in format "stat (modifier)"
    mod = math.floor((stat - 10) / 2)
    if mod >= 1:
        statStr = str(stat) + " (+" + str(mod) + ")"
    elif mod <= 0:
        statStr = str(stat) + " (" + str(mod) + ")"
    else:
        statStr = "How did you get here?"
    #Returns string with stat + modifier
    return(statStr)

#dice roller
def rollDice(sides):
    roll = random.randint(1, sides)
    return roll

def error():
    print("I'm sorry. I didn't understand that. Please try again.")
    time.sleep(0.75)
    os.system("clear")

def printClassList():
    print("Choose a class:")
    for i in classList:
        print(str(classList.index(i)+1) + ". " + i[0].upper() + i[1:].lower())

def chooseClass():
  choice = ""
  while True: 
    try:
        if choice == "":
            print()
            printClassList()
            print()
            choice = int(input(">>"))-1
            continue
        elif choice in range(len(classList)):
            os.system('clear')
            charClass = classList[choice]
            print(classList[choice][0].upper() + classList[choice][1:].lower())
            print("------------------------------------")
            print(classInfo[charClass]['description'])
            print("Starting HP: ", classInfo[charClass]['startingHp'])
            print("Primary Stat:", classInfo[charClass]['primary'])
            print()
            print("Do you want to play a", charClass + "? (y/n)")
            confirm = input("").lower()
            if confirm in ('y', 'yes'):
                choice = charClass
                break
            elif confirm in ('n', 'no'):
                choice = ""
                os.system("clear")
                continue
            else:
                error()
                continue
        else:
            choice = ""
            error()
            continue
    except ValueError:
       error()
       continue
  return choice

os.system("clear")
print("Create your character!")
print()
print("----------------")
print()
charName = input("What's your character's name? ")
charClass = chooseClass()
os.system("clear")
print()
print("Sweet! A new", charClass, "has joined the game\n")
time.sleep(0.75)
print("Give me a second to roll your stats")
time.sleep(1.5)
os.system("clear")
charStr = statRolls()
charDex = statRolls()
charCon = statRolls()
charInt = statRolls()
charWis = statRolls()
charCha = statRolls()
charHp = classInfo[charClass]['startingHp']
print(charName.upper())
print("-----------------------------------")
print()
print("Hit points:", charHp)
print("-----------------------------------")
print()
print("ABILITIES")
print("STR:", charStr)
print("DEX:", charDex)
print("CON:", charCon)
print("INT:", charInt)
print("WIS:", charWis)
print("CHA:", charCha)
import random, math, time, os, string

#dict containining classes, their starting HPs, and their descriptions
classInfo = { 
    'barbarian': { 
        'startingHp': 12, 
        'description': 'A fierce warrior who can enter a battle rage',
        'primary' : 'Strength',
        'stat' : 'Str'
    },
    'bard': {
        'startingHp': 8, 
        'description': 'An inspiring magician whose power echoes the music of creation',
        'primary' : 'Charisma',
        'stat' : 'cha'
    },
    'cleric': {
        'startingHp': 8, 
        'description': 'A priestly champion who wields divine magic in service of a higher power',
        'primary' : 'Wisdom',
        'stat' : 'wis'
    },
    'druid': {
        'startingHp': 8, 
        'description': 'A priest of the Old Faith, wielding the powers of nature and adopting animal forms',
        'primary' : 'Wisdom',
        'stat' : 'wis'
    },
    'fighter': {
        'startingHp': 10, 
        'description': 'A master of martial combat, skilled with a variety of weapons and armor',
        'primary' : 'Strength or Dexterity',
        'stat' : 'Str'
    },
    'monk': {
        'startingHp': 8, 
        'description': 'A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection',
        'primary' : 'Dexterity & Wisdom',
        'stat' : 'dex'
    },
    'paladin': {
        'startingHp': 10, 
        'description': 'A holy warrior bound to a sacred oath',
        'primary' : 'Strength & Charisma',
        'stat' : 'Str'
    },
    'ranger': {
        'startingHp': 10, 
        'description': 'A warrior who combats threats on the edges of civilization',
        'primary' : 'Dexterity & Wisdom',
        'stat' : 'dex'
    },
    'rogue': {
        'startingHp': 8, 
        'description': 'A scoundrel who uses stealth and trickery to overcome obstacles and enemies',
        'primary' : 'Dexterity',
        'stat' : 'dex'
    },
    'sorceror': {
        'startingHp': 6, 
        'description': 'A spellcaster who draws on inherent magic from a gift or bloodline',
        'primary' : 'Charisma',
        'stat' : 'cha'
    },
    'warlock': {
        'startingHp': 8, 
        'description': 'A wielder of magic that is derived from a bargian with an extraplanar entity',
        'primary' : 'Charisma',
        'stat' : 'cha'
    },
    'wizard': {
        'startingHp': 6, 
        'description': 'A scholarly magic-user capable of manipulating the structures of reality',
        'primary' : 'Intelligence',
        'stat' : 'int'
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
    statDict = {
        'stat' : stat,
        'mod' : mod,
        'statStr' : statStr
    }
    return(statDict)

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

def rollChar():
  choice = ""
  name = input("What is your character's name? ")
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
  os.system("clear")
  print()
  print("Sweet! A new", charClass, "has joined the game\n")
  time.sleep(0.75)
  print("Give me a second to roll your stats")
  Str = statRolls()
  dex = statRolls()
  con = statRolls()
  Int = statRolls()
  wis = statRolls()
  cha = statRolls()
  time.sleep(1.5)
  os.system("clear")
  charHp = classInfo[charClass]['startingHp']
  primaryStat = classInfo[charClass]['stat']
  charAC = 10 + dex['mod']
  print(name.upper())
  print("-----------------------------------")
  print()
  print("Hit points:", charHp)
  print("Primary Stat:", primaryStat.upper())
  print("AC:", charAC)
  print("-----------------------------------")
  print()
  print("ABILITIES")
  print("STR:", Str['statStr'])
  print("DEX:", dex['statStr'])
  print("CON:", con['statStr'])
  print("INT:", Int['statStr'])
  print("WIS:", wis['statStr'])
  print("CHA:", cha['statStr'])
  return {
      'name' : name,
      'class' : charClass,
      'hp' : charHp,
      'primary stat' : primaryStat,
      'ac' : charAC,
      'Str' : Str,
      'dex' : dex,
      'con' : con,
      'int' : Int,
      'wis' : wis,
      'cha' : cha,
  }

def fight(player1, player2):
    player1HP = player1['hp']
    player1Mod = player1[player1['primary stat']]['mod']
    player2HP = player2['hp']
    player2Mod = player2[player2['primary stat']]['mod']
    roundCounter = 0
    while player1HP > 0 and player2HP > 0:
        os.system("clear")
        print("Let's fight!")
        roundCounter +=1   
        print(player1['name'].upper(), "VS", player2['name'].upper() + ": ROUND", roundCounter, "\n\n")
        time.sleep(0.5)
        ##Calculate rolls for both characters
        p1RawRoll = rollDice(20)
        p1ModRoll = p1RawRoll + player1Mod
        p2RawRoll = rollDice(20)
        p2ModRoll = p2RawRoll + player2Mod
        
        ##Player 1 turn
        print(player1['name'].upper() + "'S TURN")
        print("-------------------------------------")
        input("Press any key to roll your attack!\n")
        print(player1['name'], "rolls", str(p1RawRoll), "+", str(player1Mod), " = ", str(p1ModRoll))
        if p1ModRoll > player2['ac']:
            print(player1['name'], "hits", player2['name'], "\n")
            input("Press any key to roll damage!\n")
            rawDamageRoll = rollDice(8)
            modDamageRoll = rawDamageRoll + player1Mod
            player2HP = player2HP - modDamageRoll
            print(player1['name'], "does", modDamageRoll, "(" + str(rawDamageRoll), "+" , str(player1Mod) + ") damage" )
            print(player2['name'], "has", player2HP, "hit points remaining!\n")
            input("Press any key to continue")
            print("\n\n")
        else:
            print(player1['name'], "misses!")
            print(player2['name'], "has", player2HP, "hit points remaining!\n")
            input("Press any key to continue")
            print("\n\n")

        ##Player 2 turn
        print(player1['name'].upper() + "'S TURN")
        print("-------------------------------------")
        print(player2['name'], "rolls", str(p2RawRoll), "+", str(player2Mod), " = ", str(p2ModRoll))
        if p2ModRoll > player1['ac']:
            print(player2['name'], "hits", player1['name'], "\n")
            input("Press any key to roll damage!\n")
            rawDamageRoll = rollDice(8)
            modDamageRoll = rawDamageRoll + player2Mod
            player1HP = player1HP - modDamageRoll
            print(player2['name'], "does", modDamageRoll, "(" + str(rawDamageRoll), "+" , str(player2Mod) + ")" )
            print(player1['name'], "has", player1HP, "hit points remaining!\n")
            input("Press any key to continue")
            print("\n\n")
        else:
            print(player2['name'], "misses!")
            print(player1['name'], "has", player1HP, "hit points remaining!\n")
            input("Press any key to continue")
            print("\n\n")
    print("Game Over!")
    if player1HP <=0 and player2HP <= 0:
        print("We have a draw!", player1['name'], "and", player2['name'], "have killed each other!")
    if player1HP <= 0:
        print(player2['name'], "wins in", roundCounter, "rounds!")
    elif player2HP <= 0:
        print(player2['name'], "wins in", roundCounter, "rounds!")



os.system("clear")
print("Battle Sim")
print()
print("Player One:")
print("Create your character!")
print()
print("----------------")
player1 = rollChar()
print()
print("Press any key to continue")
input()
os.system("clear")
print()
print("Player Two:")
print("Create your character!")
print()
print("----------------")
player2 = rollChar()
print()
print("Press any key to continue")
input()
os.system("clear")
fight(player1, player2)


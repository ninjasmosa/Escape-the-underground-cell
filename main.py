import sys
import random

#sets up the variables
key = "false"
safeCrack = "false"
gun = "false"
guard = "alive"
safeCode = str((random.randrange(1000,9999)))


#start the game
print("Welcome to Escape the underground cell, a text-based adventure game by ninjasmosa.")
print()
print()
print()
# If you are forking this code feel free to uncomment this part then add your credits
# print("[Credit goes here]")
print()
print("""You wake up in a prison cell. You have no idea how you got here. Maybe someone tried to take you in as a hostage. Anyway, now is not the time for questions, you need to do something.

After some thought, you decide that you should leave before anything bad happens.""")
print()
print()
print()

def start(): #the cell you start in
  choice1 = input("Will you exit through the door? 'Y' or 'N'? ")
  if choice1 == "Y":
    Corridor() #exit the cell to the corridor
  elif choice1 == "y":
    Corridor()
  elif choice1 == "N":
    print("Are you sure?")
    start()
  elif choice1 == "n":
    print("Are you sure?")
    start()
  else:
    print("I didn't understand that, try again.")
    print()
    start()


def Corridor(): #the corridor
  print()
  print("You are inside a long corridor. A door guarded by a guard is west. The office is to the east.")
  print()
  choice2 = input("Will you go to the 'door' or the 'office'? ")
  choice2 = choice2.lower()
  if choice2 == "office":
    Office() #enter the office
  elif choice2 == "door":
    Door() #walk to the door
  else:
    print("I didn't understand that, try again.")
    print()
    Corridor()


def Office(): #the office
  print()
  print("You are in a small office. A safe is inside the wall and a note lies on the desk.")
  print()
  choice3 = input("Will you look at the 'note' or inspect the 'safe'? Or will you 'leave'? ")
  choice3 = choice3.lower()
  if choice3 == "note": #look at the note
    Note()
  elif choice3 == "safe": #look at the safe
    Safe()
  elif choice3 == "leave": #leave the office
    print()
    print("You decide to leave the office.")
    Corridor()
  else:
    print("I didn't understand that, try again.")
    print()
    Office()


def Note(): #read the note
  print()
  print("""The note says:
The safe code is""")
  print(safeCode)
  Office()


def Safe(): #look at the safe
  print()
  choice4 = input("There is a tall safe. Will you try to crack the safe? 'Y' or 'N'? ")
  if choice4 == "Y": #start cracking the safe
    SafeCrack()
  elif choice4 == "y":
    SafeCrack()
  elif choice4 == "N": #leave the safe alone
    Office()
  elif choice4 == "n":
    Office()
  else:
    print("I didn't understand that, try again.")
    print()
    Safe()

def SafeCrack():
  global safeCrack
  global gun
  global key
  if safeCrack == "false":
    print()
    print("Type in the code. Type 'leave' to walk away from the safe. ") #cracking the safe
    choice5 = str(input())
    if choice5 == str(safeCode): #correct password, safe is cracked
      safeCrack = "true"
      key = "true"
      gun = "true"
      print()
      print("You cracked the safe! Inside was the door keys and a gun. With this, you leave the office.")
      Corridor()
    elif choice5 == "leave": #leave the safe alone
      Office()
    else: #password was wrong
      print("Wrong password!")
      SafeCrack()
  if safeCrack == "true": #safe is already cracked
    print("The safe is already cracked. You decide to leave the office.")
    Corridor()

def Door():
  global gun
  global guard
  if guard == "alive": #the guard is already alive
    print()
    print("Just before you take the exit, you see a tall guard in front of the door. He is holding a large machete.")
    if gun == "true": #you have a gun
      print()
      choice6 = input("Will you shoot the guard? 'Y' or 'N' ")
      if choice6 == "Y": #you shoot the guard
        guard = "dead"
        print()
        print("You shoot the guard in the head. He dies instantly.")
        Doorlock() #to the door
      elif choice6 == "y": #you shoot the guard
        guard = "dead"
        print()
        print("You shoot the guard in the head. He dies instantly.")
        Doorlock()
      elif choice6 == "N": #you walk away from the guard
        print()
        print("You decide not to shoot the guard and walk away from him.")
        Corridor()
      elif choice6 == "n": #you walk away from the guard
        print()
        print("You decide not to shoot the guard and walk away from him.")
        Corridor()
      else:
        print()
        print("I didn't understand that, try again.")
        Door()
    if gun == "false": #you have no gun
      print()
      print("You probably don't want to mess with him so you walk away.")
      Corridor()
  if guard == "dead": #guard is already dead
    print()
    print("The guard is dead. You rush towards the door.")
    Doorlock() #to the door

def Doorlock():
  global key
  print()
  print("You reach the door. It is locked.")
  if key == "true": #have a key
    choice7 = input("Will you try unlocking the door with the key? 'Y or 'N'? ")
    if choice7 == "Y": #unlock the door
      print()
      print("""The door unlocks. You hastily run outside.
      
      You are free!""")
      input("Press enter to end the game.") #ends the game
      sys.exit()
    elif choice7 == "y":
      print()
      print("""The door unlocks. You hastily run outside.
      
      You are free!""")
      input("Press enter to end the game.") #ends the game
      sys.exit()
    elif choice7 == "N": #don't unlock the door
      print()
      print("You decide to walk away from the door.")
      Corridor()
    elif choice7 == "n":
      print()
      print("You decide to walk away from the door.")
      Corridor()
    else:
      print()
      print("I didn't understand that, try again.")
      Doorlock()
  elif key == "false": #no key
    print()
    print("The door is locked and you have no key. You walk away from the door.")
    Corridor() #back to the corridor


start()

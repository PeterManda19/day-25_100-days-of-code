import random


print("⚔️   Character Stats Generator ")
print("⚔️")
print()
print("Everytime you key in your response press enter.")

def rollDice(num):
    return random.randint(1,num)


def dice_6_8():
  return rollDice(6) * rollDice(8)


def promptUser():
  while True:
    print()
    name = input("Name your warrior: ")
    
    if name.isnumeric() == True:
      print("I am expecting a name not just numbers.")
      continue
    print("Their health is: "+str(dice_6_8())+"hp")
    print()
    break


def quit():
  exit = ""
  while exit.lower() != "no" or exit.lower() != "n":  
    exit = input("Do you want to generate another health stat? ") 
    if exit.lower() == "yes" or exit.lower() == "y" or exit =="":
      name = promptUser()
      dice_6_8() 
    else:
     print()
     print("Shutting down ⚔️ Character Stats Generator...")
     break
      

def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to generate health stats.""")
    print()
    continue


if __name__=="__main__":
  name = promptUser()
  quit()
  endGame()
  
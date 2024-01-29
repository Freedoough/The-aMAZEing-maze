"""
    This is a simple maze adventure game script thing
    for the purpose of learning to code with python.
    
    I hope it's as much fun executing as it was writing it
    and experimenting with the python language.

    
    By Justin Freed


"""

import time
import random




# Introduction function
# Gets user's name, welcomes them and briefs them on the objective.

def intro():

    time.sleep(3)
    user_name = input("\nPlease enter your name: ")

    time.sleep(3)
    print("\n\nHello " + user_name + "! " + "Welcome to the aMAZEing maze!\n")
    time.sleep(3)
    print("\nYour mission is to find the Legendary Leaf of Legends.\n") #"golden leaf" TBD name kinda stupid ngl
    time.sleep(3)
    print("\nAlong the way, you will face many obstacles, and perhaps...\n")
    time.sleep(2)

    i = 0

    while i < 10:
        i += 1
        time.sleep(.75)
        print("\n")

    print("...DEATH...")

    b = 0

    while b < 7:
        b += 1
        time.sleep(.75)
        print("\n")






# Start game function
# Starts game, calls intro function, asks user if they want to start game.
# Simple if else statement for various answers.

def start_game():
    intro()
    time.sleep(3)
    choice = input("Ready to start? (y/n):")
    if choice == "y":
        start_maze()
    else:

        #Trollololol (idk why i did this lol)
        print("K, bye!")
        print("Program will end in 2000 seconds")

        c = 2000

        while c > 0:

            c -= 1
            time.sleep(1)
            print(str(c) + " seconds\n")
            



# Function of actual start of the game.
# Complete with a "loading bar" mechanism thing


def start_maze():
    
    i = 0

    while i < 5:
        i += 1
        time.sleep(1)
        print("\nLoading.. Please wait\n")
    
    time.sleep(2)
    print("\nYou emerge from the ground in a blaze of fire.\n")
    time.sleep(3)
    print("\nThe ground rumbles beneath you.\n")
    time.sleep(3)
    print("\nYou make your presence known to all...\n")
    time.sleep(3)
    print("\nYou mumble to yourself 'I have awoken'.\n")
    time.sleep(4)
    print("\nIn front of you lies a mountain.\n")
    time.sleep(3)
    print("\n** In Donald Trump's voice ** 'It's a very big mountain... The biggest in the land'\n")
    time.sleep(5)
    print("\nAt the base of the mountain is a gateway. Which seems to be made out of marble.\n")
    time.sleep(4)
    print("\nYou approach the gateway, getting bigger with every step you take towards it.\n")
    time.sleep(5)
    print("\nYou step inside said gateway.\n")
    time.sleep(3)
    print("\n")
    time.sleep(2)
    print("\nYou walk down a small corridor.\n")
    time.sleep(2)
    print("\nAt the end of which has a door with a lock on it.\n")
    time.sleep(3)
    print("\nIt's a very big lock. Probably the size of two fists.\n")
    time.sleep(3)
    print("\nYou notice a sign above the door.")
    time.sleep(2)
    print("It reads:\n")
    time.sleep(2)
    print("You shall not pass\n")
    print("Danger ahead\n")
    print("You have been warned...\n\n")
    time.sleep(4)

    CHOICE_enter_main_door()





# Prompts the user if they want to enter the main door and continues with story

def CHOICE_enter_main_door():
    
    choice = input("Do you enter? (y/n): ")

    if choice == "y":
        time.sleep(2)
        print("\nYou touch the door. You feel an intense energy pulse through you.\n")
        time.sleep(2)
        print("The lock falls off immediately.\n")
        time.sleep(4)
        print("\nYou scratch your head in confusion.\n\n")
        main_entrance()
        
    elif choice == "n":
        print("You stand at the door, refusing to open it.\n")
        print("Nothing else happens.")
        time.sleep(3)
        exit


# Main entrance sequence function

def main_entrance():
    print("\nYou step inside.\n")
    time.sleep(3)
    print("\nThe door slams behind you as you hear creepy giggling in the distance.\n")
    time.sleep(4)
    print("\nIn the direction of the giggling you see a dim light. It appears to be very small from your perspective.\n")
    time.sleep(5)
    print("\nYou hesitantly start walking towards the light.\n")  
    time.sleep(3)
    print("\nThe farther you walk, you notice the light shrinking. As if you're walking away from it.\n")
    time.sleep(5)
    print("\nYou suddenly hear faint footsteps behind you.\n")
    time.sleep(3)
    print("\nYour heart starts to race as you become anxious of who's behind you...\n")
    time.sleep(4)
    #try to italicize the "what"
    print("Or what is behind you...")
    time.sleep(3)
    print("\nYou pick up the pace into what some would call a 'speed walk'.\n")
    time.sleep(4)
    print("\nYou hear the footsteps grow louder as you head down the seemingly endless hallway.\n")
    time.sleep(5)
    print("\nYou break into a sprint.")
    time.sleep(1)
    print("IT'S GAINING ON YOU")
    time.sleep(2)
    print("\nYou turn around for a split second to catch a glimpse of what it might be.\n")
    time.sleep(3)
    print("\nYou see 2 glowing red dots about 30 feet away. As you're looking back, you misstep and faceplant into the wall.\n")
    time.sleep(6)
    print("\nYour body flops to the ground.\n")
    time.sleep(3)
    print("\nYou drift into unconsciousness. As your screen slowly fades to black...\n")
    time.sleep(3)
        
    z = 0

    while z < 10:
        z += 1
        time.sleep(1)
        print("\n")

    wake_up()






# Simple "You died" function
# Called whenever branch of storyline ends with users' death
# (tried to make it dark souls style death screen)

def you_died():
    n = 0

    while n < 10:
        n += 1
        time.sleep(.75)
        print("\n")

    print("...YOU DIED...")

    x = 0

    while x < 10:
        x += 1
        time.sleep(.75)
        print("\n")
    
    # Try again prompt 

    try_again = input("\nTry again? (y/n): ")

    if try_again == "y":
        start_game()
    else:
        exit



# Wake up function
# When user wakes up from being knocked out by their own doing

def wake_up():
    time.sleep(3)
    print("\nYou feel a sharp, throbbing pain in your head.\n")
    time.sleep(2)
    print("\nYou slowly open your eyes and into consciousness.\n")
    time.sleep(3)
    print("\nYour vision is blurred but quickly regains clearness.\n")
    time.sleep(3)
    print("\nYou notice a sign in front of you. You can barely make out the words:")
    time.sleep(2)
    print("Welcome to hell >:)")
    time.sleep(5)
    print("\n\nEvery second that passes you're more conscious. You try to move your arms.\n")
    time.sleep(4)
    print("\nYou're strapped to a wooden chair of some sort. Legs included.\n")
    time.sleep(4)

    # Choice for user to break free from chair or not

    break_free_choice = input("\n\nDo you try to break free? (y/n): ")

    if break_free_choice == "y":

        break_free_result()

    elif break_free_choice == "n":
        time.sleep(3)
        print("\nWelp. I guess that's that. You perpetually sit in the chair and slowly starve to death.\n")
        time.sleep(2)
        you_died()
    else:
        print("INVALID INPUT")
        time.sleep(2)
        wake_up()




# Function to see if user breaks free of chair
        
def break_free_from_chair():

    time.sleep(3)

    break_free = input("Enter 'b' to try and break free from the chair: ")

    if break_free == "b":

        chance = random.randint(1,2)

        if chance == 1:
            return True
        elif chance == 2:
            return False
    
    else:
        time.sleep(2)
        print("INVALID INPUT")
        break_free_result()


     

# Function that receives return value of break free prompt and goes from there

def break_free_result():
    result = break_free_from_chair() 
    if result == True:
        print("\nYou manage to brute strength your way out of the chair.\n")
        time.sleep(3)
        print("\nYou make a b-line for the door you just realized was in front of you.\n")
        time.sleep(4)
        print("\nYou try the handle. Of course it's locked, dummy.")
        time.sleep(1)
        print("JK <3\n")
        time.sleep(3)
        print("\nYou look around for other means of escape.\n")
        time.sleep(3)
        print("\nYou notice a small air duct in the back corner of the tiny room.\n")
        time.sleep(5)
        print("\nYou use your noodle, grab the chair and use it to boost yourself up.\n")
        time.sleep(5)
        print("\nYou climb up and into the vent. It's quite a tight fit.\n")
        time.sleep(3)
        
        air_vent()
        
    elif result == False:
        print("\nYou have failed to break free of the chair's grip.\n")
        time.sleep(3)
        print("\nYou yell in frustration and jiggle your arms and legs.\n")
        time.sleep(3)
        print("\nThe ruckus catches the attention of your captor.\n")
        time.sleep(3)
        print("\nYou look around the room that you're in.\n")
        time.sleep(3)
        print("\nYou notice suspiscious stains on the wall.\n")
        time.sleep(4)
        print("\nYou start to panic and try to take a closer look at the stain.\n")
        time.sleep(4)
        print("\nIt appears to be blood.\n")
        time.sleep(3)
        print("\nIn that moment of you identifying the stain for some reason..\n")
        time.sleep(2)
        print("\nYou hear gargantuan footsteps grow closer and closer every second.\n")
        time.sleep(4)
        print("\nThe door that you didn't notice before busts open.\n")
        time.sleep(3)
        entity_encounter()
        
   
# Air vent function
# When user finds the air vent and continues on

def air_vent():   
         
    print("\nYou feel claustrophobic crawling through this narrow passage that's barely wide enough to fit you.\n")
    time.sleep(5)
    print("\nYou start to crawl your way through.\n")
    time.sleep(3)
    print("\nYou can't see very well, so you feel the walls of the vent with your hands.\n")
    time.sleep(4)
    print("\nAfter crawling for a little while, both sides of the vent open up.\n")
    time.sleep(3)
    print("\nIt's a T-junction. One side goes left, and the other right.\n")
    time.sleep(3)

    user_choice = input("Which direction are you going? ('left'/'right'):")

    if user_choice == "left":
        airvent_left()
    elif user_choice == "right":
        airvent_right()
    else:
        print("INVALID INPUT")
        time.sleep(4)
        air_vent()

    # Air vent choice function - left choice
def airvent_left():
    # have this direction lead to a giant fan and have it suck the user towards it
    # the user then has to check to see if they're strong enough to escape the pull of the fan
    time.sleep(1)
    print("\nYou choose to go left.\n")
    time.sleep(2)
    print("\nYou continue to crawl down the air vent. Following every turn the path puts in front of you.\n")
    time.sleep(4)
    print("\nYou then hear a low hum noise. It grows louder as you get closer.\n")
    time.sleep(3)
    print("\nYou see light through what looks like a fan. It's moving pretty fast.\n")
    time.sleep(4)
    print("\nYou feel a pretty strong pull towards the fan.\n")
    time.sleep(3)
    print("\nYou struggle for grip against the walls of the vent.\n")
    time.sleep(2)

    escape_the_fan = input("\nEnter 'e' to try and escape the fan: ")

    chance = random.randint(1,10)


    if chance >= 5:
        print("success")
    elif chance < 5:
        print("\nThe fan's strength is no match for your puny little legs.\n")
    else:
        time.sleep(2)
        print("INVALID INPUT")
        airvent_left()


    
    time.sleep(4)
    

    # Air vent choice funtion - right choice
def airvent_right():
    print("right")
















# Entity encounter
# When user fails to break free from the chair and encounters the entity that 
# Caused them to black out

def entity_encounter():

    print("\nA humanoid creature stands in the doorway. It has 6 arms and is incredibly buff.\n")
    time.sleep(4)
    print("\nIts head comes to a point like some sort of dinosaur.\n")
    time.sleep(3)
    print("\nIt reveals its teeth as it lunges forward at you.\n")
    time.sleep(3)
    print("\nYou're gripped by 4 of its arms as you helplessly sit in the chair.\n")
    time.sleep(4)
    print("\nInches from your face, it appears to grin and opens its mouth; revealing its long, slimy, pointy black tongue to you.\n")
    time.sleep(5)
    print("\nIts breath smells like something crawled into its mouth, died, and has been decomposing in there for the past 200 years.\n")
    time.sleep(5)
    print("\nYou now realize your fate.\n")
    time.sleep(3)
    print("\n'Hey, haven't you heard of mouthwash?'")
    time.sleep(1)
    print("You heckle the creature. Hoping to get a reaction to prolong your inevitable death.\n")
    time.sleep(2)
    print("\nThe creature freezes. Looking like its processing what you said.\n")
    time.sleep(3)
    print("\nIt releases you from its grip. You get some relief for a split second.\n")
    time.sleep(3)
    print("\nIt then closes its mouth and takes a breath deeper than 'The Mariana Trench'.\n")
    time.sleep(4)
    print("\nThe mockingly smiles at you and then breaths out every square inch of oxygen out ot its system.\n")
    time.sleep(4)
    print("\nWhatever gas that coming out of it mouth is so intense, you lose the ability to breathe.\n")
    time.sleep(4)
    print("\nYou attempt to hold out as long as it takes in order to gain back the ability to breathe.\n")
    time.sleep(4)
    print("\nIt seems like an eternity before it stops. You catch your breath.\n")
    time.sleep(4)
    print("\n")    
    
    # creature breaths in users face and makes a big deal about it





# Start game initial function
#start_game()
#you_died()
#air_vent()
airvent_left()

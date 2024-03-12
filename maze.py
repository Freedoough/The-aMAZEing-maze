"""
    This is a simple maze adventure game script thing
    for the purpose of learning to code with python.
    
    I hope it's as enjoyable to run as it was to write.

            :)

    
    By Justin Freed

    To do: make seperate branch with cleaned up code
    new branch name: TBD
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
    choice = input("Ready to start? (y/n):").capitalize
    if choice == "Y":
        start_maze()
    else:

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
    print("\nIn front of you lies a very big mountain.\n")
    time.sleep(3)
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
    print("It reads:\n\n")
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
        print("\nYou try the handle. It's locked.")
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
    time.sleep(3)

    escape_the_fan = input("\nEnter 'e' to try and escape the fan: ")

    chance = random.randint(1,10)


    if chance >= 5:
        time.sleep(2)
        print("\nSuddenly, a surge of energy rushes through your body.\n")
        time.sleep(3)
        print("\nYou shimmey away from the fan.\n")
        time.sleep(2)
        print("\nYou manage to escape and head back where you came from.\n")
        time.sleep(3.5)
        airvent_back()
        
    elif chance < 5:
        print("\nThe fan's strength is no match for your puny little legs.\n")
        time.sleep(3)
        print("\nYou lose grip and get pulled into the fan blades, getting chopped up alive...\n")
        time.sleep(4)
        you_died()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        airvent_left()

    # Function for doing back to the original T junction and giving the user a choice between
    # Left and right again
def airvent_back():

    print("\nYou crawl back to the T-junction.\n")
    
    time.sleep(3)

    direction = input("\nWhich direction are you going? 'left'/'right': ")

    if direction == "left":
        airvent_left()
    elif direction == "right":
        airvent_right()
    else:
        print("INVALID INPUT")
        time.sleep(2)
        airvent_back()
    

# Air vent choice funtion - right choice

def airvent_right():
    time.sleep(2)
    print("\nYou choose to go right.\n")
    time.sleep(3)
    print("\nMaking your way down the vent, you notice another vent opening on the bottom.\n")
    time.sleep(4)
    print("\nAlong with the vent continuing straight ahead.\n")
    time.sleep(3)
    print("\nYou slowly inch your way towards it and peek down to see what's below you.\n")
    time.sleep(4)
    print("\nDirectly below the vent is a table. A closer observation reveals blood covering the top.\n")
    time.sleep(5)
    print("\nIt appears to be some sort of torture chamber, with all sorts of instruments and cabinets lining the walls.\n")
    time.sleep(5)
    print("\nRight next to the table is a drain.\n")
    time.sleep(3)
    print("\nYou wince at the thought of what goes on in this room.\n")
    time.sleep(5)
    print("\nYou continue along the vent, avoiding that room at all costs.\n")
    time.sleep(3)
    print("\nAhead you can see another vent opening on the bottom. The path also stops here.\n")
    time.sleep(4)
    print("\nMoving forward is not an option...\n")
    time.sleep(4)
    print("\nYou peek down this vent now.\n")
    time.sleep(3)
    print("\nThrough the opening you don't see much. Just a dark space.\n")
    time.sleep(3)
    print("\nYou decide to 'leap of faith' and jump down, hoping to find a way out.\n")
    
    # Escape the vent function call
    # The user escapes through the vent to find a way out
    escape_the_vent()


def escape_the_vent():
    time.sleep(4)
    print("\nYou come crashing to the ground, unaware of how high above the ground the vent was.\n")
    time.sleep(4)
    print("\nFortunately, you only take slight damage.\n")
    time.sleep(3)
    print("\nYou stand up and brush yourself off, as if nothing ever happened.\n")
    time.sleep(3)
    print("\nYou're in a hallway lined with torches.\n")
    time.sleep(3)
    print("\nYou look to the left and notice a big metal door which appears to be where you just were.\n")
    time.sleep(4)
    print("\nLooking to the right, you notice the hallway extends for some distance.\n")
    time.sleep(4)
    print("\nYou start walking in that direction, curious of what's down there.\n")
    time.sleep(4)
    print("\nAs you get closer to the end, you notice another door at the far end of the hallway.\n")
    time.sleep(4)
    print("\nYou notice that there's another opening to your left.\n")

    choice = input("\nWhat's your next move? (left/straight): ").capitalize

    if choice == "LEFT":
        left_hallway()
    elif choice == "STRAIGHT":
        straight_hallway()
    else:
        print("INVALID")
        time.sleep(2)
        escape_the_vent()

# Function for turning left in the hallway
def left_hallway():
    time.sleep(2)
    print("\nYou turn down the hallway to the left.\n")
    time.sleep(2)
    print("\nThe only thing you can see is absolutely nothing. Just pitch darkness.\n")
    time.sleep(3)
    print("\nAgainst your better judgement, you continue to walk down the hall.\n")
    time.sleep(4)
    print("\nYour next step will be your downfall unfortunately.\n")
    time.sleep(3)
    print("\nThe ground beneath you suddenly opens up like a pair of trapdoors.\n")
    time.sleep(3)
    print("\nYou feel weightless and fall for what seems like an eternity.\n")
    time.sleep(3)
    print("\nWhen in reality, you fall for about 10 seconds.\n")
    time.sleep(3)
    print("\nWithin that timeframe, you have time to think to yourself and reflect.\n")
    time.sleep(5)
    print("\nYou know you aren't surviving this fall.\n")
    time.sleep(3)
    print("\nAt the bottom of the pit are a set of very long sharp spikes that's made out of some kind of stone.\n")
    time.sleep(6)
    print("\nAlthough you don't know what happened because.....")
    time.sleep(1)
    you_died()

# Function for going straight in the hallway
def straight_hallway():
    print("\nYou continue down to the end of the hallway where you're greeted by a stone door.\n")
    time.sleep(3)
    print("\nYou push on the door slowly.\n")
    time.sleep(3)
    print("\nAs it opens, you see a dome shaped room, carved out of stone.\n")
    time.sleep(3)
    print("\nThe room seems empty, but upon further examination you notice an elevated platform lining the wall.\n")
    time.sleep(5)
    print("\nOn the ceiling of the room, you notice a shiny object.\n")
    time.sleep(3)
    print("\nYou take a few steps closer to get a better look, as you suspect it might be the 'Leaf of Legends'\n")
    time.sleep(4)
    print("\nDistracted by the shiny object, you unknowingly step on a pressure plate planted in the ground.\n")
    time.sleep(4)
    print("\nThe plate moves down as your weight is supplied to it.\n")
    time.sleep(3)
    print("\nYou then hear the sound of stones grinding together as multiple openings from every angle of the room in the walls open up.\n")
    time.sleep(5)
    print("\nWithin miliseconds, arrows covered in some sort of poison are shot out of every hole in the wall from all angles.\n")
    time.sleep(4)
    print("\nTime appears to slow down to a halt...\n")
    time.sleep(6)


    dodge = input("\nEnter 'D' to attempt to dodge the arrows being shot at you: ").capitalize

    random_num = random.randint(1,20)

    if random_num >= 10:
        dodge_success()
    elif random_num <= 9:
        
        print("\nYou unsuccessfully dodge the projectiles.\n")
        time.sleep(4)
        print("\nTime returns to normal as you get hit with an arrow in the arm.\n")
        time.sleep(3)
        print("\nThe poison starts to enter your body.\n")
        time.sleep(3)
        print("\nYou get hit with another arrow in your upper back, and then your lower back.\n")
        time.sleep(1)
        print("\nSpeeding up the process of the poison being injected into your body.\n")
        time.sleep(4)
        print("\nYou're pelted with more arrows all over your body.\n")
        time.sleep(4)
        print("\nAs the poison enters your body, you start to feel the effects.\n")
        time.sleep(4)
        print("\nGrowing weaker, you are unable to support yourself anymore.\n")
        time.sleep(4)
        print("\nYou collapse on the ground, feeling sick and weak. Unable to move.\n")
        time.sleep(4)
        print("\nAs the poison flows through your body, you slowly drift into unconsciousness.\n")
        time.sleep(4)
        you_died()
   
    else:
        print("INVALID")
        time.sleep(2)
        straight_hallway()

def dodge_success():
    time.sleep(2)
    print("\nYou successfully dodge all of the arrows in a 'Matrix'-like fashion.\n")
    time.sleep(3)
    print("\nLuckily, only one arrow per opening in the wall was fired out.\n")
    time.sleep(4)
    print("\nYou let out a sigh of relief and gather your bearings in the room.\n")
    time.sleep(4)
    print("\nYou look at the pressure plate in the floor that you stepped on to trigger the booby trap you almost died from.\n")
    time.sleep(5)
    print("\nYou shake your head at it, tauntingly.\n")
    time.sleep(4)
    print("\nLooking back up at the shiny object, you notice it's a leaf shape.\n")
    time.sleep(4)
    print("\n'Could it be?'")
    time.sleep(.5)
    print("You mumble to yourself.")
    agility_maneuver()
    
   # Function that outlines the maneuver the user must make in order to obtain the leaf 
def agility_maneuver():
    time.sleep(2)
    print("\nYou analyze the room and calculate a way to get to the ceiling.\n")
    time.sleep(3)
    print("\nLooking at the platform, and then at the leaf, you think to yourself:")
    time.sleep(3)
    print("\n'If I get enough speed, maybe I can execute a wallrun, jump, grab the platform, pull myself up.")
    time.sleep(3)
    print("'Then wallrun again, kick the wall to push myself towards the center and grab the leaf.'")
    time.sleep(5)
    print("\n")

    # Chance attempt at successfully executing the maneuver or not
    def attempt():

        user_attempt = input("\nAttempt to perform this maneuver by entering 'A': ").capitalize()

        if user_attempt == "A":

            agility_check = random.randint(0,20)

            if agility_check >= 10:
                end_game()
            elif agility_check <= 9:
                print("\nYou go to wallrun, but as you gain speed and get on the wall, you trip on a bug and you faceplant into the wall.\n")
                time.sleep(3)
                print("\nYou were unsuccessful in your attempt...\n")
                time.sleep(3)
                try_again = input("Try again?(y/n): ").capitalize()
        
                if try_again == "Y":
                    time.sleep(2)
                    attempt()
                elif try_again == "N":
                    print("\nExiting program...")
                    time.sleep(3)
                    exit
                else:
                    print("INVLAID")
                    agility_maneuver()
        else:
            print("INVALID")
            time.sleep(3)
            attempt()


    attempt()       

# Function for the end of the game and the execution of the maneuver
def end_game():
    time.sleep(2)
    print("\nYou plan out your maneuver in your head, looking at the platform, and then the wall.\n")
    time.sleep(4)
    print("\nYou let out a sharp breath, planning for the worst.\n")
    time.sleep(3)
    print("\nYou back up to the far side of the room to try to get as much speed as possible.\n")
    time.sleep(4)
    print("\n'Here goes nothing..'")
    time.sleep(2)
    print("You whisper to yourself.\n")
    time.sleep(5)
    print("\nYou sprint as fast as you can towards the other side of the room.\n")
    time.sleep(3.5)
    print("\nAs you approach the underside of the platform, you jump and land your feet on the wall, keeping your feet in motion to not lose momentum.\n")
    time.sleep(5)
    print("\nYou push off the wall and reach your arm out to the edge of the platform, gripping it as tight as you can.\n")
    time.sleep(4)
    print("\nYou twist your body to face the wall and get your other hand on the platform.\n")
    time.sleep(4)
    print("\nYou manage to pull yourself up onto the platform.\n")
    time.sleep(4)
    print("\nNearly out of breath, you stand yourself up and get your bearings again.\n")
    time.sleep(4)
    print("'One part down, one to go.'")
    time.sleep(1.5)
    print("You whisper to yourself again.\n")
    time.sleep(3)
    print("\nYou do the same thing, this time running parallel to the wall.\n")
    time.sleep(4)
    print("\nYou pick up speed and jump, planting your feet on the wall.\n")
    time.sleep(3)
    print("\nBeing careful not to lose speed, you push off the wall and twist your body towards the center of the room.\n")
    time.sleep(5)
    print("\nAs you're middair, you can see the leaf within your grasp.\n")
    time.sleep(3)
    print("\nTime slows down, you reach out for the leaf as it's inches away from your hand.\n")
    time.sleep(4)
    print("\nYou then feel it's soft texture in your hand and 'firmly grasp it'.\n")
                                                    # Spongebob reference ^^^
    time.sleep(4)
    print("\nAs you feel that you have it, you do a backflip with the momentum you have form pushing off the wall.\n")
    time.sleep(5)
    print("\nGravity pulls you down, and you heroically come smashing to the ground in a 'superhero landing'.\n")
    time.sleep(4)
    print("\nYou take a moment to realize what you've achieved and stand back up.\n")
    time.sleep(4)
    print("\nTaking a look at the leaf, it starts to glow and gets brighter and brighter.\n")
    time.sleep(4)
    print("\nThe light transfers through your body and you feel an immense sensation that's been transferred toi you through the leaf.\n")
    time.sleep(5)
    print("\nThe feelings subsides after a few moments. You hold out your hands in front of you, feeling the power you just obtained.\n")
    time.sleep(5)
    print("'I did it..'")
    time.sleep(1.5)
    print("You say to yourself.\n")
    time.sleep(5)
    congratulations()


# Congratulating the user on successfully finding the leaf and obtaining it
def congratulations():

    i = 0

    while i < 10:
        i += 1
        time.sleep(.75)
        print("\n")

    print("CONGRATULATIONS!\n")
    time.sleep(4)
    print("You found the leaf and completed the objective!")

    time.sleep(4)

    play_again = input("Play again? (y/n): ").capitalize()

    if play_again == "Y":
        start_game()
    elif play_again == "N":
        time.sleep(5)
        print("Thanks for playing!")
        time.sleep(2)
        exit
    else:
        print("INVALID")
        time.sleep(2)
        print("(it doesn't matter anymore!)")
        time.sleep(2)
        print("Goodbye :)")
        time.sleep(2)
        exit


# Entity encounter
# When user fails to break free from the chair and encounters the entity that 
# Caused them to black out

def entity_encounter():


    print("\nA humanoid creature with a lizard-like face, pointed nose and viscious looking teeth stands in the doorway.\n")
    time.sleep(4)
    print("\nIts nose comes to a point like some sort of dinosaur.\n")
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
    time.sleep(1.5)
    print("You heckle the creature. Hoping to get a reaction to prolong your inevitable death.\n")
    time.sleep(2)
    print("\nThe creature freezes. Looking like its processing what you said.\n")
    time.sleep(3)
    print("\nIt releases you from its grip. You get some relief for a split second.\n")
    time.sleep(3)
    print("\nIt then closes its mouth and takes a breath deeper than 'The Mariana Trench'.\n")
    time.sleep(4)
    print("\nThe mockingly smiles at you and then breaths out every square inch of oxygen out of its system.\n")
    time.sleep(4)
    print("\nWhatever gas that coming out of it mouth is so intense, you lose the ability to breathe.\n")
    time.sleep(4)
    print("\nYou attempt to hold out as long as it takes.\n")
    time.sleep(3)
    print("\nIt seems like an eternity before it stops. You catch your breath.\n")
    time.sleep(4)
    print("\nThe creature snarls and looks at you with the attitude of a 16 year-old girl.\n")
    time.sleep(1)
    print("\n") 
    time.sleep(4)
    print("\n'You don't like that?' The creature mutters to you.\n")
    time.sleep(3)
    print("\n'Dude, what even are you? You look like the offspring of godzilla and the T-rex from 'Jurassic Park'.")
    time.sleep(1)
    print("You reply.")
    time.sleep(4)
    print("\n'Hm.. Dinner that can roast me. Funny. I'll remember that when I rip your arms out of their sockets and slap you with them after I kill you.")   
    time.sleep(4)
    print("\nYou feel the hairs on the back of your neck stand up.\n")
    time.sleep(3)
    print("\nBut you don't show your fear to the creature.\n")
    time.sleep(3)
    print("\nI'm not scared of you...")
    time.sleep(1)
    print("You mutter back.\n")
    time.sleep(3)
    print("\nWithout hesitation, the creature opens its' mouth and lunges towards your face.\n")
    time.sleep(4)
    print("\nYour head gets engulfed in the mouth of the creature.\n")
    time.sleep(3)
    print("\nThere's nothing you can do except sit and await your fate.\n")
    time.sleep(3)
    
    you_died()




# Start game initial function
start_game()

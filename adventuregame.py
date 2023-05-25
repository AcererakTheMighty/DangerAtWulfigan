""""""
#Assignment: Adventure Game, or: DANGER AT THE WULFWIGAN WINTER FORTRESS
#Author: Landon Smith
#For: Christopher Keers' Computer Science class

#copyright Bajookieland Studios and Brigham Young University-Idaho

""""""

#Player begins the game and gets their two choices on what to do
def start_game():
    print("DANGER AT THE WULFWIGAN WINTER FORTRESS")
    print("After climbing the Impossible Mountains and fighting the draugr that prowl the mountainside, you have found yourself before three ornate doors. You know not of where each leads. One could lead to death or it could lead to salvation.")
    print("Which door do you choose, brave and foolish adventurer? Do you choose (1, 2, 3)")

    choice = get_valid_input(" > ", ["1", "2", "3"])

    if choice == "1":
        enter_door_1()
    elif choice == "2":
        enter_door_2()
    elif choice == "3":
        enter_door_3()
    else:
        print("That is not an option! Cease this toomfoolery or I shall lay a curse upon thee!")
        start_game()

#Player chooses what to do in the option of the cave.
def enter_door_1():
    print("The cave is blacker than the night. You can hear faint moans and groans, shackles clink about like the chains of prisoners. Who knows what lays in these dark tunnels where the bats screech like banshees?")
    print("You see a luminescent treasure chest, glowing as bright as the sun shines.")
    print("What do you do? (1. Open the chest, 2. Leave the cave 3. Shout into the darkness for no discernable reason)")

    choice = get_valid_input("> ", ["1", "2" "3"])

#Decided to throw in some trademark black humor into this.

    if choice == "1":
        print("The chest has nothing but a piece of paper inside. You read it and it says 'Behind you!' Before you can react, you see a skeleton with an axe slam its blade into your head, killing you instantly. So ends your story, at the hand of perhaps the spookiest (and sillest) of enemies.")
        game_over()
    elif choice == "2":
        print("You make the wise decision and leave this accursed cave where you would have surely perished at the hands of the evil dead.")
        win_game()
    elif choice == "3":
        print("You shout into the darkness like a wild banshee for no discernable reason. This infuriates the ghosts in the darkness so much that a ghost dressed like a pirate comes out of nowhere and gives you directions to get out of this dungeon.")
        secret_option_2()
    else:
        print("Cease again!.")
        enter_door_1()

#Player decides what to do in the lush garden of evil

def enter_door_2():
    print("You enter a lush garden filled with all manners of fruits and vegetables, perhaps the most appetizing you have ever seen. In the corner you see a statue of what seems to be a wizard in a robe and a starry conical hat.")
    print("You see a path leading to the Wulfwigan Winter Fortress itself, standing tall and gloomy in the grey blizzards that obscure it from your sight.")
    print("What do you do? (1. Follow the path, 2. Explore the garden 3. Check out that sick wizard statue!)")

    choice = get_valid_input("> ", ["1", "2", "3"])

    if choice == "1":
        print("You walk along the path and reach the Wulfwigan Winter Fortress.")
        win_game()
    elif choice == "2":
        print("You decide to explore the garden. You walk over to the statue of the wizard and touch a button you have found on its nose. The statue suddenly disintegrates, revealing it to be an evil wizard! Before you can pull out your blade, the Wizard shouts 'SKIDDADDLE SKIPLODE, I MAKE YOU EXPLODE!' and you explode with a meaty pop. You have died!")
        game_over()
    elif choice == "3":
        print("You walk over to the wizard statue and you swing your blade at it, chopping its head off. Surprisingly, a fountain of blood emerges from the stump where the head once lay, revealing that it wasn't a statue, it was an evil wizard in waiting trying to get another victim! You take the wand it dropped and you walk on to the fortress")
        win_game()
    else:
        print("Cease at once! I have laid one curse upon thee, you now have the countenance of a horned toad, good luck getting thy ladies and fair maidens now, you most uncouth individual!")
        enter_door_2()

# The Player walks into a room that's somewhere between that one room in David Lynch's "Twin Peaks" and Tim Burton's "Beetlejuice"

def enter_door_3():
    print("You find yourself in a room with a checkered floor, red curtains, a chaise lounge chair, and a furious looking woman sitting on a chair scribbling on some paper. What do you do? 1. Talk to the woman in the chair 2. Sit in the chaise lounge chair. 3. Walk through the door")

    choice = get_valid_input("> ", ["1", "2", "3"])

    if choice == "1":
        print("You walk up to the woman who looks at you like you stepped on her puppy, burnt her shoe collection, and called her fat. Before you say a word, she turns into a giant snake demon and bites you in half. You have died!")
        game_over()
    elif choice == "2":
        print("You sit in the chaise lounge chair and sink deep into it, falling into an endless void of black. You have...died? To be fair it's not entirely clear whether you die in the Void, sometimes you just fall for eternity and you go mad.")
        secret_option_1()
    elif choice == "3":
        print("You just decide to make like a tree and leave. Good choice on your part, that lady looks immensely relieved that you are gone, and that chaise lounge chair, you swear it just winked at you!")
        win_game()


#Game over screen

def game_over():
    print("You have suffered a most terrible fate, dear traveler. Would you like to play again? (yes or no)")

    choice = get_valid_input("> ", ["yes", "no"])

    if choice == "yes":
        start_game()

#secret option number 1

def secret_option_1():
    print("You fall for hours, and suddenly you crash. You find yourself at the very bottom of the Impossible Mountains, and you have to make the journey back up to the very top again. Would you dare go travel to the top again?")

    choice = get_valid_input("> ", ["yes", "no"])

    if choice == "yes":
        start_game()

#secret option number 2

def secret_option_2():
    print("Turns out, you've been dead this whole time! Congratulations, you fool! You have fallen for the classic Byronic Protagonist Blunder!")
   
    choice = get_valid_input("> ", ["yes", "no"])

    if choice == "yes":
        start_game()

#the "CONGLATURATIONS! [sic]" Screen

def win_game():
    print("After leaving, you find a trail that you continue following until you find yourself at the Wulfwigan Winter Fortress itself, where I the great lich-king Frontrow, have been awaiting your arrival. I invite you inside, where we have our feast and I deliver unto you your reward. Congratulations, traveler, your struggles were worth it! Would you like to play again? (yes or no)")

    choice = get_valid_input("> ", ["yes", "no"])

    if choice == "yes":
        start_game()

#Code to define what a valid input is

def get_valid_input(prompt, valid_choices):
    choice = input(prompt)
    while choice not in valid_choices:
        print("Cease this toomfoolery or I shall lay a curse upon thee!")
        choice = input(prompt)
    return choice


start_game()

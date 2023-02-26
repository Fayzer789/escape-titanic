# Author : Fayzer789
import time


key = 0

a = 0
b = 0.2
c = 0.8

# Introduction


def intro():
    time.sleep(a)
    print("zzzzzzzzzzzzzzzzzzzzzzzzzz")
    time.sleep(a)
    print("DRINGGGGGGG")
    print("zzzzzzzzzzzzzzzzzzzzzz")
    print("DRINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
    time.sleep(a)
    print("Damn it can't you let me sleep just a little bit man")
    time.sleep(a)
    print("*you disable the alarm*")
    time.sleep(a)
    print("*You scratch your eyes with your hands for a bit and get up*")
    time.sleep(a)
    print("Fuck off I was getting extra good sleep if only that damn thing hadn’t woken me up")
    time.sleep(a)
    print("*You look at the window")
    time.sleep(a)
    print("Oh that's weird why is it already the night?")
    time.sleep(a)
    print("Wait")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("Don't tell me")
    time.sleep(a)
    print("............")
    time.sleep(a)
    print("IT'S ALREADY 9 PM")
    time.sleep(a)
    print("I’M 20 MINUTES LATE FOR THE BIG CRUISE MEAL")
    time.sleep(a)
    print("*you dress so fast that you have completely forgotten your tie*")
    time.sleep(a)
    print("I hope I won't be in late")
    time.sleep(a)
    print("*you're running as fast you can to not get too late*")
    time.sleep(a)
    print("...But")
    time.sleep(a)
    print("suddenly a loud noise is heard..")
    time.sleep(a)
    print("BAMMMMMMMMMM")
    time.sleep(a)
    print("It was a sudden collision that made the whole ship vibrate")
    time.sleep(a)
    print("Lights go off and a piercing red alarm starts to ring in your ears")
    time.sleep(a)
    print("Shit what's going on here?!!!")
    time.sleep(a)
    print("Speaker : hello everyone I am the captain, I have unfortunate news for you all, the ship just hit an iceberg and that received reckless damage..")
    time.sleep(a)
    print("Tss this dumbass of captain how he got in the middle of an iceberg bigger than his gut")
    time.sleep(a)
    print("Speaker : I want to tell you that there are rescue boats available")
    time.sleep(a)
    print("Ahhh finnally a good new ")
    time.sleep(a)
    print("Speaker : But only for women and children")
    time.sleep(a)
    print("What??? this is not fair at all")
    time.sleep(a)
    while True:
        choice = input("What choices do you want to make? 1 for still going to the rescue boats or 2 to let the rescue boats for the others people ")
        if choice == "1":
            print()
            choice1()
        elif choice == "2":
            print()
            choice2()
        else:
            print("Please enter a valid option")


def choice1():
    time.sleep(a)
    print("They really think I’d stand here and do nothing")
    time.sleep(a)
    print("*You decided to still going to the rescue boats*")
    print("Oh damn I don't know the plan of this ship")
    back()


def back():
    print("There are two doors in front of you")
    while True:
        choice = input("Hmmm which door should I take? Type left or right ")
        if choice.lower() == "left":
            left()
        elif choice.lower() == "right":
            right()
        else:
            print("Please enter a valid option")


#
def left():
    print("you took the left door that leads you to the hallway")
    print("You see a window and decide to look through it")
    print("Maybe I should jump in the water it would be easier")
    print("..Even if there’s a great chance of... dying ")
    while True:
        choice = input("Should I jump through the window or continue my way? Type window or walk ")
        if choice.lower() == "window":
            window()
        elif choice.lower() == "walk":
            walk()
        else:
            print("Please enter a valid option")


def window():
    print("Well here we go")
    print("*You open the window and take a deep breath*")
    print("*slap face* you can do it " + mc_name)
    print(mc_name + "YOU.. CAN.. DO.. IT")
    print("A rush of adrenaline rises in you and you finally decide to jump")
    print("SPLASHHHHHHHHHHHH")
    print("Your body didn't support the shock")
    dead_screen()


def walk():
    print("You choose to keep walking")
    print("*In the end of the hallway you see a door*")
    while True:
        choice = input("Hmm should I open this door? Type Yes or No ")
        if choice.lower() == "yes":
            while True:
                choice = input("You see a drunken sailor in there with a key ring, should you ask him politely or knock him out? Type ask or ko ")
                if choice.lower() == "ask":
                    ask()
                elif choice.lower() == "ko":
                    knockout()
                else:
                    print("Please enter a valid option")

        elif choice.lower() == "no":
            while True:
                choice = input("Are you sure? you're gonna walk back to the hallway. Type Yes or No ")
                if choice.lower() == "yes":
                    print("Maybe it's not a great idea to go to this door")
                    print("You decided to walk back to the hallway")
                    left()
                else:
                    print("Please enter a valid option")
        else:
            print("Please enter a valid option")


def ask():
    print("Hello sir it was to know if I-")
    print("WHAT DO YOU WANTTT")
    print("Nothing nothing I-")
    print("WHY ARE YOU COMING WHEN I'M DRINKING?!!")
    print("I don't know it was a coincid- ")
    print("COINCIDENCE MY ASS YOU'RE TRYING TO ROB ME THAT'S THE ONLY REASON WHY YOU ARE THERE")
    print("No no no you're wrong I-")
    print("I WONT LET YOU TO ROB ME")
    print("the sailor pulled a knife")
    print("Oh fuckkk noo noo no I-")
    print("The sailor is running to you")
    print("Shitttt what should I do??")
    while True:
        choice = input("Run away or try to fight back? Type run or fight ")
        if choice == "run":
            run()
        elif choice == "fight":
            fight()
        else:
            print("Please enter a valid option")


def run():
    print("Sorry to bother you I’m leaving")
    print("*You're trying to run as fast you can but you see the sailor to get closer to you")
    print("I'M COMING DUMBASS")
    print("OM MY GOD NO NO NO")
    print("He finally catch you up takes you with one arm and throw you away through the window")
    dead_screen()


def fight():
    print("YOU KNOW WHAT MAN YOU DON'T EVEN AFRAID ME")
    print("COME ON")
    print("*You get into combat position and you’re getting closer to him*")
    print("I DID 2 YEARS OF BOXING WHEN I WAS A KID YOU ARE NOT THAT SCA-")
    print("PAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    print("He hit you in the face so hard that you had a heart attack")
    dead_screen()


def knockout():
    print("He hasn’t seen me yet and drunk as he is will only bring trouble")
    print("My only option it's to make him fall asleep for a moment")
    print("*You hide behind the furniture and sneak to get to him*")
    print("Wait what am I doing...")
    print("Maybe instead to knock him I could ask him")
    print("Even if he’s drunk maybe he will understand")
    while True:
        global key
        choice = input("Do you want to ask him or still knock him out? Type ask or ko ")
        if choice.lower() == "ask":
            ask()

        elif choice.lower() == "ko":
            print("No he is too drunk to ask him anything")
            print("You sneak up behind him and jump on his neck to strangle him")
            print("WHAT ARE YOU DOING???")
            print("AHHHHHHHHHHHHHHH")
            print("I CAN'T BREATH ANYMORE")
            print("*You knock out the sailor*")
            print("Pfiouu it was exhausting")
            print("*You take out the keychaind and put into your pocket*")
            key += 1
            print("You wall back into the hallway")
            back()

        else:
            print("Please enter a valid option")


def right():
    global key
    print("You try to open the door")
    print("*door closed*")
    print("Rahhh I need a key")
    if key == 0:
        back()

    elif key == 1:
        print("Oh wait I have one")
        sos_door()


def sos_door():
    print("*you take out the keychain and open the door*")
    print("I knew it would help me")
    print("*You see a panel filled with dust, you take it and try to dust it down to make it a little more readable*")
    print("What is even written on this panel")
    print("E..mer..gen..cy pa..t..h fo..r fli..g..ht c.re..w")
    print("!!!")
    print("Emergency path especially for flight crew!!!!")
    print("Then they have an emergency path just for them these lazy")


def choice2():
    time.sleep(a)
    print("Well they are not wrong, there must be people who need it more than me")
    time.sleep(a)
    print("You decided to let the rescues boats for the others people")


# dead screen
def dead_screen():
    print("        *****************************************")
    print("        *                                       *")
    print("        *            You are DEAD               *")
    print("        *                                       *")
    print("        *****************************************")


def end_screen():
    print("        *****************************************")
    print("        *          You finished the game!       *")
    print("        *                Congrats               *")
    print("        *****************************************")


# main screen
print("        *****************************************")
print("        *                                       *")
print("        *            Escape Titanic             *")
print("        *                                       *")
print("        *****************************************")
time.sleep(a)
mc_name = input("What's your name? ")
time.sleep(a)
print("Welcome", mc_name, "You are currently in the TITANIC so don't worry everything's gonna be fine :)  ")
time.sleep(a)
while True:
    start_game = input("Are you ready ? ")
    if start_game.lower() == "no" or start_game == "No":
        print("Okay maybe next time")
    elif start_game.lower() == "yes" or start_game == "Yes":
        intro()
    else:
        print("Please enter a valid option")

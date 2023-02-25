mc_name = input("What's your name?")
print("Welcome", mc_name, "you are currently in a boat that just hit an iceberg, your goal is to get out of here in LIFE ")

answer = input(
    "You can only turn left or right, Which way would you go? Be careful the wrong path might lead you to a painful death" ).lower()

if answer == "left":
    answer = input("You walked into a room and there’s an open window, you can either jump out of there hoping to get out alive or walk down the hall? Type jump to jump out of the window or walk to walk down the hall")

    if answer == "jump":
        print("You drowned and you died. Did you really think you could survive?")

    elif answer == "walk":
        answer = input("You arrive in front of a room either you walk back or you enter")
        if answer == "walck back":
            print()
        elif answer == "enter":
            answer = input("You see a drunken sailor who has a key ring, you either politely ask him for his keys or you knock him out and retrieve them")
            if answer =="ask":
                answer = input("You kindly ask him to give you his keys but he suddenly becomes aggressive, try to calm him down or you confront him")

            elif answer == "Knock him out":
                print("lol")
            else:
                print("Not a valid option")

    else:
        print("Not a valid option, you're dead")

elif answer == "right":
    print("")

else:
    print("Not a valid option, you're dead")
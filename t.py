import sys, time

Game1dict = {'Character Name': 'James',
             'Character age': '16',
             'Gender': 'Boy',
             'Personality': 'Prideful, Arrogant, Understanding, Thoughtful',
             'Extra': 'Gamer, Volunteers at local charity',
             'Current Ally': 'Best friend, Luke',
             'Ally Name': 'Luke',
             'Ally age': '15',
             'Ally Gender': 'Boy',
             'Ally Personality': 'Nerdy, Hard Working, Laid Back',
             'Ally Extra': 'Chore Boy, Braces, Always carries a computer, Borrows grandmas glasses',
             'Background': 'Your house is seen on fire from the TV in Luke\'s house. you rush home as fast as you can, only to find... your house perfectly intact. You must have mistaken another house for yours. Your house may not be on fire but something is different. Your mom has left a note and is not home. The note reads - \n        Come to Billy\'s Burritos at 3:00 A.M. or I\'ll have to kill your mom. \n        P.S. Bring me money to buy a burrito'
             }

Items = []


def decide(choice1, choice2, output1, output2):
    print('\n - ' + choice1 + '\n\nor\n')
    print(' - ' + choice2 + '\n')
    while True:
        decision = input('Choose a path (1 or 2) \n')
        if decision == '1' or decision == '2':
            break
        elif decision.lower() == 'items':
            print()
            for x in Items:
                print(' - ' + x)
            print()
        else:
            print('Please use a number for your answer')
    if decision == '1':
        print(output1)
        return 1
    else:
        print(output2)
        return 2


def Main():
    print(
        'Welcome to PathLithe. This game consists of different games (Currently 1 game). Typing "items" will give you a list of your current items during the game. Hope you enjoy!\n')
    GameDict = Game1dict
    print(
        f'Game 1 -\n\n    Main Character Bio - \n    Character Name: {GameDict["Character Name"]}\n    Character age: {GameDict["Character age"]}\n    Gender: {GameDict["Gender"]}\n    Description - \n        Personality: {GameDict["Personality"]}\n        Extra: {GameDict["Extra"]}\n    Current Ally: {GameDict["Current Ally"]}\n\n    {GameDict["Ally Name"]} Bio - \n        Character age: {GameDict["Ally age"]}\n        Gender: {GameDict["Ally Gender"]}\n        Description - \n           Personality: {GameDict["Ally Personality"]}\n           Extra: {GameDict["Ally Extra"]}\n\n    Background: {GameDict["Background"]}')
    while True:
        gameMode = input('\nType the number of the game you would like to play - ')
        try:
            if int(gameMode) == 1:
                Game1()
                break
            else:
                print('Game mode chosen is out of range')
        except:
            print('Your answer was invalid, please use a number for your answer')


def Game1():
    num = decide('I don\'t care about my mom', 'I must go find my mom',
                 'You sit at home for the next few hours playing video games',
                 'You\'ve decided you need to rescure your mom')
    if num == 1:
        # Not saving mom
        print('You\'ve decided it\'s not worth it for your mom')
        num = decide('Mom isn\'t here , I can stay up', 'i should go to sleep', '', '')
        if num == 1:
            # Stay up
            print('You stay up on video games, until you hear a knock on the door')
            num = decide('I guess I should answer the door', 'I shouldn\'t answer the door',
                         'You walk down stairs and open the door...',
                         'You stay where you are listening for any more knocks')
            if num == 1:
                # Answer door
                print('to be stabbed in the chest')
            else:
                # Don't answer the door
                print('Then you hear another knock, even louder. Suddenly they are banging on the door')
                num = decide('Fine I\'ll answer the door', 'I should call 911', 'You answer the door to...',
                             'You pick up your phone and call 911')
                if num == 1:
                    # Finally answer door
                    print('an angry man who pins you down and stabs you ferociously')
                else:
                    # Call 911
                    print('"911 what\'s your emergency" comes from the phone')
                    num = decide('Give your address', 'Give the emergency', 'You tell them your adress...',
                                 'You tell them the emergency...')
                    if num == 1:
                        # Give your address
                        print('but you\'re dragged away from the phone')
                        num = decide('Fight back', 'Don\'t resist', 'You try to resist but get silenced by a knife',
                                     'You allow yourself to get dragged...')
                        if num == 2:
                            print(
                                'and find yourself in the kitchen. You are slowly stabbed and feel your concious ebbing away')
                            time.sleep(3)
                            print('You awake in a hospital bed with an iv')
                            print(
                                'The news is then broke to you that your mom is dead. Atleast, thanks to you, the murderer has been caught and sentenced to jail for 32 years with parole')
                    else:
                        # Give the emergency
                        print(
                            'but don\'t get a chance to tell them your address as you\'re pulled back and muted by the intruder')
                        num = decide('Fight back', 'Don\'t resist', 'You try to resist but get silenced by a knife',
                                     'You allow yourself to get dragged...')
                        if num == 2:
                            print('but then get slowly stabbed to death')
        else:
            # Go to sleep
            print('You never woke up again')
    else:
        # Saving mom
        print('You walk through the house thinking...')
        num = decide('I should leave now, theres no telling what could happen', 'I still have time to plan this out',
                     'Alright!, let\'s go', 'Alright! I need paper...')
        if num == 1:
            # Leave now
            pass
        else:
            # Plan it out
            print('You find paper in the printer to use, and a pen in a drawer (You aquired two items)')
            Items.append('Paper')
            Items.append('Pen')
            num = decide('Should I do what he says', 'Maybe I should be a hero',
                         'Let\'s get a snack and a phone (Two items aquired)', 'Let\'s get lots of supplies')
            if num == 1:
                # Get snack and phone (Follow note)
                print('After grabbing those few things, you leave for Billy\'s Burritos, but should you walk or drive')
                Items.append('Snack')
                Items.append('Phone')
                num = decide('I should drive my car', 'I\'ll just walk there',
                             'You\'ve decided driving is the best options',
                             'Walking may turn out for the better, you think')
                if num == 1:
                    # Drive car
                    print('You start up the car and start the drive to Billy\'s Burritos')
                    num = decision('', '', '', '')
                else:
                    # Walk
                    pass

            else:
                # Try to be hero (Getting lots of supplies)
                pass


Main()
sys.exit()
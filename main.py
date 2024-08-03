import time
import random


def pause(msg):
    time.sleep(1)
    print(msg)


def house():
    global health
    pause('You suddenly caught a whiff of freshly baked bread.')
    pause('Enter 1 if you want to follow the smell.')
    pause('Enter 2 if you want to turn around and leave.')
    while True:
        time.sleep(2)
        game_choice_1 = input('Which will you choose? ')
        if game_choice_1 == '1':
            pause("You've chosen to follow the bread smell.")
            pause("A house appears from the dark.")
            pause("You walk up to it and knock on the door.")
            pause(
                "A nice old lady comes out to greet you and hands you a "
                'freshly baked loaf of bread.'
            )
            pause("You thank her and eat it to replenish your health.")
            pause("Health +30")
            health += 30
            pause(f'Current Health: {health}')
            break
        elif game_choice_1 == '2':
            pause("You get a sense that smell is a trap. You turn around.")
            pause("You hear a low rumbling and realize it's your stomach.")
            pause("Your energy is low as you continue to travel.")
            pause("Health -20")
            health -= 20
            pause(f'Current Health: {health}')
            break
        else:
            pause("Invalid choice. Please enter 1 or 2.")


def cave():
    global health
    pause('A cave appears in front of your path.')
    pause("It's too dark to see inside.")
    pause("You wonder what dangers may lay ahead.")
    pause('Enter 1 if you bravely enter the dark cave.')
    pause('Enter 2 if you run the other way.')
    while True:
        time.sleep(2)
        game_choice_1 = input('Which will you choose? ')
        if game_choice_1 == '1':
            pause("You head into a cave and get swarmed by bats.")
            pause("You duck immediately to avoid the bats.")
            pause("They fly over and leave you unharmed.")
            pause("The cave dead ends.")
            pause("You turn around to leave.")
            pause(f'Current Health: {health}')
            break
        elif game_choice_1 == '2':
            pause("You turn left to avoid the cave.")
            pause("You tripped and over a rock.")
            pause("You're injured and suffered some health loss.")
            pause("Health -30")
            health -= 30
            pause(f'Current Health: {health}')
            break
        else:
            pause("Invalid choice. Please enter 1 or 2.")


def fight():
    global health
    opponent = random.choice(['wolf', 'bear', 'jaguar'])
    pause(f'A giant {opponent} runs up to you. '
          f'Its eyes glowing in the dark '
          f'and bears its teeth at you.')
    pause(f'Enter 1 if you decide to fight the {opponent}.')
    pause(f'Enter 2 if you decide to befriend the {opponent}.')
    while True:
        time.sleep(2)
        game_choice_1 = input('Which will you choose? ')
        if game_choice_1 == '1':
            pause("You frantically search on the ground for a weapon.")
            pause(f"You find a rock and throw it at the {opponent}.")
            pause("It jumps at you and knocks you to the ground."
                  f'It leans in to sniff you.'
                  f"It decides that you're not worth its time.")
            pause("It scoffs and hops away into the dark forest.")
            pause("You took a health hit and get back up.")
            pause("Health -30")
            health -= 30
            pause(f'Current Health: {health}')
            break
        elif game_choice_1 == '2':
            pause("You slowly walk up to it. "
                  f'and reach out your hand to show no harm.')
            pause("It sniffs at your hand cautiously and gives it a lick.")
            pause("It lowers its head and you go to pet it.")
            pause("You've gained a traveling companion!")
            pause("You feel invigorated by this new friend!")
            pause('Gain health +20.')
            health += 20
            pause(f'Current Health: {health}')
            break
        else:
            pause("Invalid choice. Please enter 1 or 2.")


def play_game():
    global health
    health = 50
    name = input('Enter your name: ')

    print(
        f'Hi, {name}! You find yourself in a dark forest, where you can '
        'barely see your hand in front of your face.'
    )
    pause('Everything is lit by moonlight only.')
    pause(
        "You notice that you're traveling alone, and you're only at 50 of "
        '100 max health.'
    )
    pause("You cautiously venture ahead to try to get out of the dark forest.")

    scenarios = [house, cave, fight]
    random.shuffle(scenarios)

    for scenario in scenarios:
        pause('You keep moving forward.')
        scenario()
        if health <= 0:
            pause("GAME OVER.")
            pause("You lost all your health and did not survive the forest.")
            pause(f"Better luck next time, {name}.")
            break

    if health > 0:
        pause("You have enough health to leave the darkforest!")
        pause(f"Congratulations, {name}! You've won!")


while True:
    play_game()
    while True:
        time.sleep(2)
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            break
        else:
            pause("Invalid input. Please enter 'y' or 'n'.")
    if play_again == 'n':
        break

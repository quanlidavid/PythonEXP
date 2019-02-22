from sys import exit


def dead(why):
    print(why,"Good job!")
    exit(0)


def gold_room():
    print("This room is full of gold. How much do you take?")

    choise=input("> ")
    if "0" in choise or "1" in choise:
        how_much=int(choise)
    else:
        dead("Man, learn to type a number.")

    if how_much<50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another doo")
    print("How are you going to move the bear?")
    bear_moved=False

    while True:
        choice = input("> ")

        if choice=="take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

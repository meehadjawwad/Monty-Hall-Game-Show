# importing the library
import random

# creating a list of doors
doors = [1, 2, 3]

# introducing user to the rules of the game
print()
print("Welcome to the Monty Hall Game show!")
print()
print("There are three doors in front of you: 1, 2, and 3.")
print()
print("Behind one of them is a car, and the other two are empty.")
print()
print("If you pick the one with the car, you win the car.")
print("If you pick one which is empty, you win nothing.")
print()
print("Good luck!")
print()

# the computer picks a 'winning door' at random
winning_door = random.choice(doors)
doors.remove(winning_door)

# asking the user to pick a door
choice = int(input('Please pick one of the doors (1, 2, 3): '))

# assigning individual names to all the doors so that they can be referred to later in the code
if choice != winning_door:
   doors.remove(choice)
   third_door = random.choice(doors)
else:
   second_door = random.choice(doors)
   doors.remove(second_door)
   third_door = random.choice(doors)

# mid-point in the game
print()
print("Good! So you have picked door number", choice)
print()
print("Let's make the game a little more interesting.")
print()

# the final phase of the game
# i'm aware that some of the code is redundant, but i wanted to maintain the same structure throughout
if choice != winning_door:
    print("I can tell you that, door", third_door, "is empty.")
    print("That means, the prize is either behind door", choice, "or door", winning_door)
    print()
    print("I'll give you the option to switch from door", choice, "to door", winning_door)
    print()
    ans = input("Do you want to make the switch? (yes or no): ")
    print()
    if ans == 'yes':
        choice = winning_door
        print("You have now picked door number", winning_door)
        print()
        print("Let's open it and see if you've won.")
        print()
        if choice == winning_door:
            print("Congratulations! You have won the car.")
        else:
            print("Sorry, door number", choice, "is empty.")
            print("The car was behind door number", winning_door)
    else:
        print("You have decided to stick with door", choice)
        print()
        print("Let's open it and see if you've won.")
        print()
        if choice == winning_door:
            print("Congratulations! You have won the car.")
        else:
            print("Sorry, door number", choice, "is empty.")
            print("The car was behind door number", winning_door)

else:
    print("I can tell you that, door", third_door, "is empty.")
    print("That means, the prize is either behind door", choice, "or door", second_door)
    print()
    print("I'll give you the option to switch from door", choice, "to door", second_door)
    print()
    ans = input("Do you want to make the switch? (yes or no): ")
    print()
    if ans == 'yes':
        choice = second_door
        print("You have now picked door number", second_door)
        print()
        print("Let's open it and see if you've won.")
        print()
        if choice == winning_door:
            print("Congratulations! You have won the car.")
        else:
            print("Sorry, door number", choice, "is empty.")
            print("The car was behind door number", winning_door)
    else:
        print("You have decided to stick with door", choice)
        print()
        print("Let's open it and see if you've won.")
        print()
        if choice == winning_door:
            print("Congratulations! You have won the car.")
        else:
            print("Sorry, door number", choice, "is empty.")
            print("The car was behind door number", winning_door)

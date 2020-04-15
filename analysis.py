import random

result = []


def play_monty(choice, decision):
    doors = [1, 2, 3]
    winning_door = random.choice(doors)

    if choice != winning_door:
        if decision == 'switch':
            result.append(1)
        elif decision == 'stay':
            result.append(0)

    elif choice == winning_door:
        if decision == 'switch':
            result.append(0)
        elif decision == 'stay':
            result.append(1)


def monty_switch(x):
    for i in range(1, x):
        choice = 1
        decision = 'switch'
        play_monty(choice, decision)
    print("\nIf a computer plays", x, "games and decides to stay with its choice, the results are as follows:")
    print(result)
    print("The computer has won", sum(result), "times.")
    print("The winning probability is {a:2.2f}%\n".format(a=(sum(result) / x) * 100))
    result.clear()


def monty_stay(x):
    for i in range(1, x):
        choice = 1
        decision = 'stay'
        play_monty(choice, decision)
    print("\nIf a computer plays", x, "games and decides to stay with its choice, the results are as follows:")
    print(result)
    print("The computer has won", sum(result), "times.")
    print("The winning probability is {a:2.2f}%\n".format(a=(sum(result) / x) * 100))
    result.clear()


monty_switch(1000)
monty_stay(1000)
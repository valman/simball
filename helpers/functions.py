import random


def choose_action(actions):
    # Return an action based on chance
    roll = random.random() * 100
    chosen = "Undecided"
    c = 0

    # print(f"The actions are {actions}")

    for action, chance in actions:
        c += chance
        # print(f"Roll is {roll} for {action}")
        if roll < c:
            return action

    # In case of rounding issues, return the last action
    return actions[-1][0]

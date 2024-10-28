#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: elon <-- Noah Sonne Kargo
"""
import random

"""
function: take_turn()
This function lets a player take a turn in the 1-die game.

As demonstrated in class, a player turn requires the player to
make at least one roll of the die.  If the player rolls a 1,
then the turn ends and any points earned during the turn are lost.  
If the player rolls anything else, then the player can choose to 
keep rolling or to stop.  When the player chooses to stop, the
player earns the sum of all rolls this turn.

After each roll that is not a one, prompt the player to type "r" or "R"
to keep rolling; typing anything else ends the turn.

For each roll, print the result of that roll and the total score
so far.  Make sure it is clear which is which; don't just print
numbers without any context.

Return the number of points earned on the turn.

Note: the initial code given would be just return 0
"""


def take_turn():
    # if all you do here is roll one die one time, you are wrong.
    # your code here
    total_score = 0
    dice_roll = True
    while dice_roll:
        roll = random.randrange(1, 7)

        if roll == 1:
            print("You roll a 1")
            return 0

        total_score += roll
        current_score = total_score
        print(f'You rolled {roll}')

        if total_score == 0:
            dice_roll = False
            return total_score

        print(f'Your current score is {current_score}')

        choice = input("Do you want to roll again? (r/R): ")
        if choice == 'r' or 'R':
            continue
        else:
            return total_score



"""
function: play_one_turn_pig()
- This function is already completed.  Inspect it to help you
  implement the next function.
- This function lets a player play a very short Pig game, which
  ends after exactly 1 turn.
"""


def play_one_turn_pig():
    print('1-Turn Pig Time!')
    score = take_turn()
    print('You scored', score)


"""
function: play_solitaire_pig()
This function lets a player play a solitaire Pig game.

Prompt the player for a target score, then let the player
take turns until they reach or exceed that score. You can assume
the player will only enter integers, but make sure you don't let
them enter a negative target score. This function must call take_turn.

Print "Solitaire Pig Time!" before starting the game,
print the player's score and turn number after each turn, and
print the final score and the number of turns taken when the 
game ends. Again,make sure it is clear what is being printed.
"""


def play_solitaire_pig():
    print('Solitaire Pig Time!')

    total_score = 0
    target_score = int(input('Enter your target score: '))

    while total_score < target_score:
        turn_score = take_turn()
        total_score += turn_score

        if turn_score == 0:
            print("Turn ended with a score of 0.")

    print(f'Congratulations! You reached or exceeded the target score of {target_score} with a total score of {total_score}.')



"""
function: play_heads_up_pig()
This function lets 2 players play a heads-up Pig game.

This should proceed the same way as solitaire except alternating
between player 1 and player 2.  Again, don't allow negative target
scores. If player 1 exceeds the target score, then player 2 gets 
one more turn before the game ends.  If player 2 exceeds the target 
score, then the game ends right away. This function must call take_turn.

Print "Heads-up Pig Time!" before starting the game,
print which player's turn it is before starting the turn,
print each player's score and the round number at the end of
the round, and print both scores at game end.

"""


def play_heads_up_pig():
    print('Heads-up Pig Time!')

    player1_score = 0
    player2_score = 0

    target_score = int(input("Enter your target score: "))

    while player1_score < target_score or player2_score < target_score:

        print("\nPlayer 1's Turn:")
        player1_roll = take_turn()
        player1_score += player1_roll
        print(f"Player 1's total score is now {player1_score}.")

        if player1_score >= target_score:
            print(f"Player 1 wins with a score of {player1_score}!")
            return player1_score, player2_score


        print("\nPlayer 2's Turn:")
        player2_roll = take_turn()
        player2_score += player2_roll
        print(f"Player 2's total score is now {player2_score}.")


        if player2_score >= target_score:
            print(f"Player 2 wins with a score of {player2_score}!")
            return player1_score, player2_score



''' Change no code below here '''




''' Here be dragons '''




''' Don't change this '''


def start():
    games = {
        't': ('1-Turn Pig', play_one_turn_pig),
        's': ('Solitaire Pig', play_solitaire_pig),
        'h': ('Heads-up Pig', play_heads_up_pig),
    }
    print('Menu\n----')
    for (key, game) in games.items():
        print(key, ": ", game[0], sep='')
    choice = input('\nGame choice: ')
    if choice in games:
        games[choice][1]()
    else:
        print('Sorry, that is not a game choice')


if __name__ == '__main__':
    start()

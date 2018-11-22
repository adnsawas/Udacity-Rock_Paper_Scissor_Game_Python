#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
short_moves = ['r', 'p', 's']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def convert_human_input(short_move):
    if short_move == 'r':
        return 'rock'
    elif short_move == 'p':
        return 'paper'
    else:
        return 'scissors'


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.their_last_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_last_move = random.choice(moves)

    def move(self):
        return self.their_last_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_last_move = random.choice(moves)

    def move(self):
        if self.my_last_move == 'rock':
            return 'paper'
        elif self.my_last_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class HumanPlayer(Player):
    def move(self):
        # Get human input
        human_input = input('Play (p) for paper, (r) for rock, '
                            + '(s) for scissors OR '
                            + '(q) for ending the game: ').lower()
        if human_input in short_moves:
            return convert_human_input(human_input)
        elif human_input == 'q':
            return 'q'
        else:
            print('You entered an invalid character.')
            return self.move()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        # Checking if a human entered q to quit the game.
        if (move1 == 'q') or (move2 == 'q'):
            return 'exit'
        print(f"Player 1: {move1}  Player 2: {move2}")
        # Checking the winner
        if beats(move1, move2):
            self.p1.score = self.p1.score + 1
            print("Player 1 won!")
        elif beats(move2, move1):
            self.p2.score = self.p2.score + 1
            print("Player 2 won!")
        else:
            print("TIE!")
        # Print scores
        print(f"Scores: (Player 1: {self.p1.score}),  "
              + f"(Player 2: {self.p2.score})")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"\n=================Round {round + 1}==================")
            roundValue = self.play_round()
            if roundValue == 'exit':
                print('Ending game. Calaculating results...')
                break

        # Announce the winner
        print('\n\n=====================================\n'
              + '=====================================\n'
              + 'Game Final Results are:')
        print(f'Player 1: {self.p1.score},   Player 2: {self.p2.score}')
        if self.p1.score > self.p2.score:
            print('Player 1 is THE WINNER!')
        elif self.p1.score < self.p2.score:
            print('Player 2 is THE WINNER!')
        else:
            print('It\'s a TIE. NO WINNER!')
        print("\nThe game is over!\n"
              + '=====================================\n'
              + '=====================================\n')


def select_computer_mode():
    computer_mode = input('Select the computer play style '
                          + '(random, reflect, cycle): ').lower()
    if computer_mode == 'random':
        return Game(HumanPlayer(), RandomPlayer())
    elif computer_mode == 'reflect':
        return Game(HumanPlayer(), ReflectPlayer())
    elif computer_mode == 'cycle':
        return Game(HumanPlayer(), CyclePlayer())
    else:
        print('You entered an invalid play style.')
        return select_computer_mode()


if __name__ == '__main__':
    # Prompt the user to select which mode the computer will play.
    game = select_computer_mode()
    game.play_game()

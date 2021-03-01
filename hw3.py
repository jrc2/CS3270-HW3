#!/usr/bin/env python3

"""
Main module for the q-learning assignment
"""

__author__ = 'John Chittam'
__version__ = 'Spring 2021'

import random
from move_directions import MoveDirections


class QLearning:
    """
    The main class for the q-learning assignment
    """
    # Q(s, a) = Q(s, a) + (reward + max_a Q(s’, a))
    ALPHA = 0.1  # learning rate
    GAMMA = 0.9  # discounts future rewards
    EPSILON = 0.1
    DEATH = -25
    GOAL = 150

    q_table = {
        ('A', MoveDirections.RIGHT): 0,
        ('A', MoveDirections.DOWN): 0,
        ('B', MoveDirections.RIGHT): 0,
        ('B', MoveDirections.DOWN): 0,
        ('B', MoveDirections.LEFT): 0,
        ('C', MoveDirections.RIGHT): 0,
        ('C', MoveDirections.DOWN): 0,
        ('C', MoveDirections.LEFT): 0,
        ('D', MoveDirections.RIGHT): 0,
        ('D', MoveDirections.DOWN): 0,
        ('D', MoveDirections.LEFT): 0,
        ('E', MoveDirections.DOWN): 0,
        ('E', MoveDirections.LEFT): 0,
        ('F', MoveDirections.UP): 0,
        ('F', MoveDirections.RIGHT): 0,
        ('F', MoveDirections.DOWN): 0,
        ('G', MoveDirections.UP): 0,
        ('G', MoveDirections.RIGHT): 0,
        ('G', MoveDirections.DOWN): 0,
        ('G', MoveDirections.LEFT): 0,
        ('H', MoveDirections.UP): 0,
        ('H', MoveDirections.RIGHT): 0,
        ('H', MoveDirections.DOWN): 0,
        ('H', MoveDirections.LEFT): 0,
        ('I', MoveDirections.UP): 0,
        ('I', MoveDirections.RIGHT): 0,
        ('I', MoveDirections.DOWN): 0,
        ('I', MoveDirections.LEFT): 0,
        ('J', MoveDirections.UP): 0,
        ('J', MoveDirections.DOWN): 0,
        ('J', MoveDirections.LEFT): 0,
        ('K', MoveDirections.UP): 0,
        ('K', MoveDirections.RIGHT): 0,
        ('K', MoveDirections.DOWN): 0,
        ('L', MoveDirections.UP): 0,
        ('L', MoveDirections.RIGHT): 0,
        ('L', MoveDirections.DOWN): 0,
        ('L', MoveDirections.LEFT): 0,
        ('M', MoveDirections.UP): 0,
        ('M', MoveDirections.RIGHT): 0,
        ('M', MoveDirections.DOWN): 0,
        ('M', MoveDirections.LEFT): 0,
        ('N', MoveDirections.UP): 0,
        ('N', MoveDirections.RIGHT): 0,
        ('N', MoveDirections.DOWN): 0,
        ('N', MoveDirections.LEFT): 0,
        ('O', MoveDirections.UP): 0,
        ('O', MoveDirections.DOWN): 0,
        ('O', MoveDirections.LEFT): 0,
        ('P', MoveDirections.UP): 0,
        ('P', MoveDirections.RIGHT): 0,
        ('Q', MoveDirections.UP): 0,
        ('Q', MoveDirections.RIGHT): 0,
        ('Q', MoveDirections.LEFT): 0,
        ('R', MoveDirections.UP): 0,
        ('R', MoveDirections.RIGHT): 0,
        ('R', MoveDirections.LEFT): 0,
        ('S', MoveDirections.UP): 0,
        ('S', MoveDirections.RIGHT): 0,
        ('S', MoveDirections.LEFT): 0,
        ('T', MoveDirections.UP): 0,
        ('T', MoveDirections.LEFT): 0,
    }

    grid = (
        (('A', 0), ('B', 0), ('C', 0), ('D', 0), ('E', 0)),
        (('F', 0), ('G', 50), ('H', DEATH), ('I', 105), ('J', 0)),
        (('K', 0), ('L', 75), ('M', 0), ('N', -1), ('O', -5)),
        (('P', 15), ('Q', 0), ('R', 0), ('S', 0), ('T', GOAL))
    )

    block_row = 0
    block_column = 0
    curr_block = 'A'
    done = False
    MAX_COL = len(grid[0]) - 1
    MAX_ROW = len(grid) - 1

    def __init__(self):
        while not self.done:
            self.random_move()

    def random_move(self):
        # random.seed(0)
        moved = False
        while not moved:
            direction = random.randint(0, 3)
            # if direction == 1:
            #     print(direction)
            moved = self._move(direction)

    def _move(self, direction):
        """
        Moves Wolfie to a new block in the grid

        :param direction: {MoveDirections} the direction to move
        :return: {bool} true if successfully moved, false if that move
                 direction is not possible
        """
        if direction == MoveDirections.UP:
            if self.block_row == 0:
                return False
            self.block_row -= 1
        elif direction == MoveDirections.RIGHT:
            if self.block_column == self.MAX_COL:
                return False
            self.block_column += 1
        elif direction == MoveDirections.DOWN:
            if self.block_row == self.MAX_ROW:
                return False
            self.block_row += 1
        elif direction == MoveDirections.LEFT:
            if self.block_column == 0:
                return False
            self.block_column -= 1
        else:
            return False

        self.curr_block = self.grid[self.block_row][self.block_column][0]
        reward = self.grid[self.block_row][self.block_column][1]
        if reward == self.GOAL or reward == self.DEATH:
            self.done = True
        print('block: ' + self.curr_block)  # temp print statement to see if this is working

        return True


if __name__ == '__main__':
    QLearning()
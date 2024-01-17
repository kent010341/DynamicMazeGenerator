import numpy as np
from typing import List, Tuple

## constants
MAZE_SIZE = (5, 5)
# Probability of "wall-breaking" at the dead end
MUTATION_RATE = 0.1
WALL = 1
PATH = 0
UNDEFINED = -1

def init_maze(size: Tuple[int]) -> np.ndarray:
    """
    Initialize the maze with all cells set to -1 (undefined) using NumPy.

    :param size: Size of the maze
    :return: Initialized maze as a 2D NumPy array
    """
    return np.full(size, UNDEFINED)

def choose_entrance(size: Tuple[int]) -> Tuple[int]:
    """
    Randomly choose one point at one of the borders as entrance.

    :param size: Size of the maze
    :return: row and col
    """

    row_size, col_size = size
    if np.random.rand() > 0.5: # Top or bottom
        row = np.random.choice([0, row_size - 1])
        col = np.random.randint(1, col_size - 1)
    else: # Left or right
        row = np.random.randint(1, row_size -1)
        col = np.random.choice([0, col_size -1])

    return (row, col)

def generate_maze(size: Tuple[int]) -> np.ndarray:
    """
    Generate a maze using NumPy, with random walk and mutation when hitting a dead end.

    :param size: Size of the maze
    :return: Generated maze as a 2D NumPy array
    """
    maze = init_maze(size)
    entrance = choose_entrance(size)
    maze[entrance] = PATH

    return maze

def main():
    maze = generate_maze(MAZE_SIZE)
    print(maze)

if __name__ == '__main__':
    main()

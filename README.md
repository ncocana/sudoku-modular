# Sudoku Modular

**Table of contents**

-   [**How to play Sudoku**](#how-to-play-sudoku)
-   [**How Sudoku was adapted**](#how-sudoku-was-adapted)
-   [**Credits**](#credits)

## How to play Sudoku

[Sudoku](http://en.wikipedia.org/wiki/Sudoku) is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9.

## How Sudoku was adapted

For this project, the game was generalized and simplified.

A procedure ([checkSudoku](https://github.com/ncocana/sudoku-modular/blob/main/src/checkSudoku.py)) was defined, which takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:

1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
2. Each row of the square contains each of the whole numbers from 1 to n exactly once.

You may assume that the input is square and contains at least one row and column.

## Credits

Code from [dfleta](https://github.com/dfleta/Python_ejercicios/tree/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/sudoku).  
I just refactored and organized the project.

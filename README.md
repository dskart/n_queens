# N Queens Problem

This is the code of a solver for the n-queens problem, wherein n queens are to be placed on an n×n chessboard so that no pair of queens can attack each other. Recall that in chess, a queen can attack any piece that lies in the same row, column, or diagonal as itself.

Here is the explanation for the [8-queen](https://en.wikipedia.org/wiki/Eight_queens_puzzle) variant

This was made as an exercise to implement a depth-first graph search algorithm in order to solve a puzzle. So please take in account that this code was written in a few days without any professional review/standard .

## Getting Started

The file ["n_queens.py"](n_queens.py) contains all the code and depth-first algorithm to solve our puzzle.

## Running the solver

The following function will give you back a python iterator with the solutions for a board of size "n", you can then cycle through the solutions with "next()".

```[python]
solutions = n_queens_solutions(4)
next_solution = next(solution)
```

## Authors

- **Raphael Van Hoffelen** - [github](https://github.com/dskart) - [website](https://www.raphaelvanhoffelen.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

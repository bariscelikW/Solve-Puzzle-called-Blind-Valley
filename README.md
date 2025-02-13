# Tiling Puzzle Solver

This project is a Python implementation of a backtracking algorithm to solve a tiling puzzle based on given constraints. The program reads input from a file, processes the board and constraints, and outputs the solution to another file.

## How It Works

The algorithm uses backtracking to place H (Horizontal) and B (Black) tiles on a board while satisfying given row and column constraints. It validates each move and ensures no adjacent tiles violate the rules.


## Input Format

The input file consists of:

1. A row of integers representing the required number of H tiles in each row.

2. A row of integers representing the required number of B tiles in each row.

3. A row of integers representing the required number of H tiles in each column.

4. A row of integers representing the required number of B tiles in each column.

5. A grid representing the board layout using characters:

   - L: Left part of a horizontal tile

   - U: Upper part of a vertical tile

   - D: Lower part of a vertical tile

   - N: Empty space
  

## Example Input File (i1.txt)
```
2 -1 -1
-1 -1 2
-1 2 -1 -1
-1 -1 -1 0
L R L R
U U L R
D D L R
```

## Output Format

The output file contains the solved board, with each row written as space-separated values.

### Example Output File (o1.txt)
```
B H B H
H B N N
B H B H
```
### If no solution exists, the program outputs:
```
No solution!
```


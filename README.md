# Tiling Puzzle Solver

This project is a Python implementation of a backtracking algorithm to solve a tiling puzzle based on given constraints. The program reads input from a file, processes the board and constraints, and outputs the solution to another file.

## How It Works

The algorithm uses backtracking to place H (Horizontal) and B (Black) tiles on a board while satisfying given row and column constraints. It validates each move and ensures no adjacent tiles violate the rules.

## Algorithm Explanation

### 1. Input Parsing

- The program reads an input file containing:

   - Constraints on how many H and B tiles must be in each row and column.

   - A board layout with predefined tile positions (L, U, D, N).

### 2. Board Representation

- The board is represented as a 2D list (ans), initialized with zeros.

- The algorithm iterates over this board to fill the tiles while ensuring constraints are met.

### 3. Constraint Validation

The algorithm uses multiple helper functions to validate moves:

- ```is_valid(ans, r, c, k, column_length, row_length)``` Ensures a tile placement does not violate adjacency rules.

- ```is_valid_for_horizontal(ans, r, c, l, column_length)``` Ensures horizontally placed tiles do not repeat within the board constraints.

- ```is_valid_for_vertical(ans, r, c, l, column_length)``` Ensures vertically placed tiles do not repeat within the board constraints.

- ```check_boundaries(ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length)``` Checks whether the placed tiles match the given row and column constraints.

### 4. Backtracking Solver

- The function ```solve(...)``` attempts to fill the board recursively:

   - If the board is completely filled ```(r == row_length)```, it verifies the constraints.

   - If the current cell is L, it attempts placing (H, B), (B, H), or (N, N).

   - If the current cell is U, it attempts placing (H, B) or (B, H) in a vertical fashion.

   - If the current cell is D, it moves forward without modifying.

   - The function backtracks if a solution is not found.


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


import sys

def is_valid(ans, r, c, k, column_length, row_length):
    # check up side and left side, dont need to check right and downside
    if k == 'N':
        return True

    if r == 0 and c == 0:
        return True
    elif r == 0 and c != column_length - 1:
        return ans[r][c - 1] != k 
    elif 0 < r < row_length - 1 and c == 0:
        return ans[r - 1][c] != k
    elif 0 < r < row_length - 1 and c != 0:
        return ans[r - 1][c] != k and ans[r][c - 1] != k
    elif r == row_length - 1 and c == 0:
        return ans[r - 1][c] != k
    elif r == row_length - 1 and c != 0:
        return ans[r - 1][c] != k and ans[r][c - 1] != k

    return True

def is_valid_for_horizontal(ans, r, c, l, column_length):
    # L R U  
    # L R D  in this situation, we cant check R D's values just using is_valid()
    # this function created for checking this siuation
    if l == 'N' or ans[r][c] == 'N':
        return True

    if c != column_length - 2 and ans[r][c + 2] == l:
        return False
    return True

def is_valid_for_vertical(ans, r, c, l, column_length):
    #   U
    # U D
    # D  for this situations
    if l == 'N' or ans[r][c] == 'N':
        return True
    if c != column_length - 1 and ans[r][c + 1] == l:
        return False
    return True

  
def check_boundaries(ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length):
    for i in range(row_length):
        h_ctr = sum(1 for j in range(column_length) if ans[i][j] == 'H') # find H numbers in rows
        b_ctr = sum(1 for j in range(column_length) if ans[i][j] == 'B') # find B numbers in rows

        # if it is not suit return false
        if H_row_extension[i] != -1 and H_row_extension[i] != h_ctr:
            return False
        elif B_row_extension[i] != -1 and B_row_extension[i] != b_ctr:
            return False

    for i in range(column_length):
        h_ctr = sum(1 for j in range(row_length) if ans[j][i] == 'H') # find H numbers in columns
        b_ctr = sum(1 for j in range(row_length) if ans[j][i] == 'B') # find B numbers in columns

        # if it is not suit return false
        if H_column_extension[i] != -1 and H_column_extension[i] != h_ctr:
            return False
        elif B_column_extension[i] != -1 and B_column_extension[i] != b_ctr:
            return False
    # if we come here, it means correct
    return True

def solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, r = 0, c = 0):
    # backtracking function
    # if r equals row lengths it means our board is full, check boundries
    if r == row_length and check_boundaries(ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length):
        return ans.copy()  
    
    elif c == column_length:
        return solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, r + 1, c = 0)
    
    try:
        
        if board[r][c] == 'L':
            # iterate throught values from given list
            for k in [('H', 'B'), ('B', 'H'), ('N', 'N')]:
                left_val, right_val = k[0], k[1]
                # if values is correct, continue
                if is_valid(ans, r, c, left_val, column_length, row_length) and is_valid_for_horizontal(ans, r, c, right_val, column_length):
                    # changed ans with values
                    ans[r][c] = left_val
                    ans[r][c + 1] = right_val
                    # recursion part
                    result = solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, r , c + 2)
                    if result:
                        return result
                    # if func. returns false go back
                    ans[r][c] = 0
                    ans[r][c + 1] = 0

        #nearly same execution with upper part, just change downside index
        elif board[r][c] == 'U':
            for k in [('H', 'B'), ('B', 'H'), ('N', 'N')]:
                left_val, right_val = k[0], k[1]
                if is_valid(ans, r, c, left_val, column_length, row_length) and is_valid_for_vertical(ans, r, c, left_val, column_length):

                    ans[r][c] = left_val
                    ans[r + 1][c] = right_val
                    result = solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, r, c + 1)
                    if result:
                        return result
                    ans[r][c] = 0
                    ans[r + 1][c] = 0
        #when encountered with D, call function with c + 1
        elif board[r][c] == 'D':
            result = solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, r, c + 1)
            if result:
                return result
            
    # if we encountered with list index out of range, check boundries
    except IndexError:
        if check_boundaries(ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length):
            return ans.copy()
    # if we come here, it means there is no solution
    return None

def open_files():

    # open input and output files
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    my_input = input_file.readlines()
    # read input files, and define variables
    H_row_extension = [*map(int, my_input[0].split())]
    B_row_extension =[*map(int, my_input[1].split())]
    H_column_extension = [*map(int, my_input[2].split())]
    B_column_extension = [*map(int, my_input[3].split())]
    column_length = len(H_column_extension)
    row_length = len(H_row_extension)
    # define board from given input
    board = [list(line.strip().split()) for line in my_input[4:] if line.strip()]
    input_file.close()
    # create ans list 
    ans = [[0 for _ in range(column_length)] for _ in range(row_length)]
    # find solution
    my_res = solve(board, ans, H_row_extension, B_row_extension, H_column_extension, B_column_extension, column_length, row_length, 0, 0)

    # if there is answer, print line by line else: print there is no solution
    if my_res:
        for indexs in range(len(my_res)):
            if indexs != len(my_res) - 1:
                output_file.write(" ".join(map(str, my_res[indexs])) + "\n") # Write each row with a newline character
            else:
                output_file.write(" ".join(map(str, my_res[indexs])))
    else:
        output_file.write("No solution!")

    # close output file
    output_file.close()

def main():
    # call functions
    open_files()

if __name__ == "__main__":
    main()
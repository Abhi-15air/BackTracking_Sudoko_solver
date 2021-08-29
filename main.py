suduko_board = [
    [0,0,0,0,0,8,0,0,1],
    [0,2,0,4,5,0,0,6,8],
    [0,0,1,7,0,6,4,0,0],
    [0,0,0,0,0,0,2,0,5],
    [0,1,0,0,0,0,0,4,0],
    [7,0,9,0,0,0,0,0,0],
    [0,0,8,2,0,7,9,0,0],
    [4,7,0,0,9,5,0,8,0],
    [2,0,0,1,0,0,0,0,0]
]


count = 0

 #we slove here recursively
def solve_recursively_board(game_board):


    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  # showing all the steps
    # print()
    # print_board(suduko_board)


    global count     #displaying the number of steps taken by backtracking algorithm

    count = count + 1

    find = find_empty_position(game_board)
    if not find:   #this is base case
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validity(game_board, i, (row, col)):
            game_board[row][col] = i

            if solve_recursively_board(game_board):  #calling recursively
                return True

            game_board[row][col] = 0

    return False


def validity(game_board, num, pos):
    # Check row validity
    for i in range(len(game_board[0])):
        if game_board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column validity
    for i in range(len(game_board)):
        if game_board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3 * 3 submatrices validity
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if game_board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(game_board):
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(game_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(game_board[i][j])
            else:
                print(str(game_board[i][j]) + " ", end="")


def find_empty_position(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0:
                return (i, j)  # row, col in form of tuple

    return None
print("SLOVE SUDOKO GAME BOARD:")
print_board(suduko_board)
solve_recursively_board(suduko_board)
print("****************************")
print("SLOVED SUDOKO BOARD")
print_board(suduko_board)

print("No of steps taken by backtracking algorithm to slove the sudoko board")
print(count)
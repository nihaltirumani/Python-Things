import random

def print_state():
    for x in range(9):
            if (x + 1) % 3 == 0:
                print(grid[x])
            else:
                print(grid[x], end=" ")

def replace(option, char):
    grid.pop(option)
    grid.insert(option, char)

def check_win_state(win_pos, win_char):
    global running
    if grid[win_pos[0]] == win_char and grid[win_pos[1]] == win_char and  grid[win_pos[2]] == win_char:
        print_state()
        print(f"{win_char} WON!!!")
        running = False
    

def check_win():
    global running
    chars = ["X", "O"]
    full = 0

    for char in chars:
        check_win_state([0,1,2], char)
        check_win_state([3,4,5], char)
        check_win_state([6,7,8], char)
        
        check_win_state([0,3,6], char)
        check_win_state([1,4,7], char)
        check_win_state([2,5,8], char)

        check_win_state([0,4,8], char)
        check_win_state([2,4,6], char)

    
    if running == True:
        for cell in grid:
            if cell != " ":
                full += 1
        if full == 9:
            running = False
            print("Draw")
    
def ask_user():
    global player_option

    try:
        player_option = int(input("please select option (1-9): ")) - 1
    except Exception as e:
        print("Invalid input")
        ask_user()
    
    if player_option > 9 or player_option < 0 :
        print("Invalid position.")
        ask_user()

empty_grid = [" " for i in range(9)]
grid = empty_grid.copy()
player_option = None
bot_option = random.randint(0,8)
counter = 0
running = True

while running:
    if counter % 2 == 0:
        ask_user()
    else:
        while not grid[bot_option] == " ":
            bot_option = random.randint(0,8)

        replace(bot_option, "O")
        counter += 1
        print_state()
        player_option = "A"
    
    if player_option != "A":

        if grid[player_option] != " " :
            print("You can't place on already placed one.")
        elif grid[player_option] == " ":
            replace(player_option, "X")
            counter += 1

    check_win()
from random import randint
import pygame
import time
pygame.init()

# First function that also calls other functions that, as we will see, make the table for the game
def minesweeper(n,bombs):
    table = make_table(n)
    table = add_bombs(table,bombs)
    table = change_table(table)
    return table

# The function make_table creates an nxn array of zeros that is the first edition of the gameboard
def make_table(n):
    return [[0]*n for i in range(n)]
# This function randomly assigns bombs to the table
def add_bombs(table,bombs):
    for i in range(bombs):
        is_bomb = False
        while not is_bomb:
            x = randint(0, len(table) - 1) # chooses a random x-coordinate on the table
            y = randint(0, len(table) - 1) # chooses a random y-coordinate
            if table[x][y] != 9:# checks that there is not already a bomb in place
                table[x][y] = 9 # places the bomb at this location (assigned as the value 9)
                is_bomb = True
    return table

# This function changes the rest of the table/gameboard values depending on where the newly placed bombs are. 
def change_table(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] == 9:
                table = check_down_left(table,x,y)
                table = check_down_right(table,x,y)
                table = check_down(table,x,y)
                table = check_up_left(table,x,y)
                table = check_up_right(table,x,y)
                table = check_up(table,x,y)
                table = check_right(table,x,y)
                table = check_left(table,x,y)
    return table

# The following functions go through each location on the table and check to see if that location is "touching" a bomb.
# For each bomb that a location touches, that location gets a +1 value added to it.
def check_down_right(table,x,y):
    if x + 1 < len(table[x]) and y - 1>= 0: #these intial 'if' statements ensure that the checked location exists on the table
        if table[x+1][y-1] != 9:
            table[x+1][y-1] += 1
    return table

def check_up_right(table,x,y):
    if x + 1 < len(table[0]) and y + 1 < len(table):
        if table[x+1][y+1] != 9:
            table[x+1][y+1] += 1
    return table

def check_right(table,x,y):
    if x + 1 < len(table[0]):
        if table[x+1][y] != 9:
            table[x+1][y] += 1
    return table

def check_down_left(table,x,y):
    if x - 1 >= 0 and y - 1 >= 0:
        if table[x-1][y-1] != 9:
            table[x-1][y-1] += 1
    return table

def check_up_left(table,x,y):
    if x - 1 >= 0 and y + 1 < len(table):
        if table[x-1][y+1] != 9:
            table[x-1][y+1] += 1
    return table

def check_left(table,x,y):
    if x - 1 >= 0:
        if table[x-1][y] != 9:
            table[x-1][y] += 1
    return table

def check_down(table,x,y):
    if y - 1 >= 0:
        if table[x][y-1] != 9:
            table[x][y-1] += 1
    return table

def check_up(table,x,y):
    if y + 1 < len(table):
        if table[x][y+1] != 9:
            table[x][y+1] += 1
    return table
# This function just allowed me to check and see that the table was created correctly.
def pr(table):
    for i in table:
        print (i)
# This is a class for the entire gameboard being displayed
class Board:
    def __init__(self,board):
        self.board = board
    def __repr__(self): # __repr__ represents the object as a string
        pr(self.board)
        
        return 

# This class represents each square on the gameboard
class Square:
    def __init__(self,x,y,w,h,board,ij):
        self.rect = pygame.rect.Rect(x,y,w,h) # Provides the dimensions for the squares
        i,j = ij
        self.val = board[i][j] # Provides the numeric value of a specific square on the board
        self.x = x
        self.y = y
        self.visible = False
        self.flag = False

def restart(n,bombs):
    game(n,bombs)

# This function opens the nearby squares of value zero (touching zero bombs) upon initially clicking a zero square
def open_game(first, square): 
    square.visible = True
    i,j = square.x//40,square.y//40
    if i + 1 < len(first): # First checks that the square touching the current square is in the table
        if first[i+1][j].visible == False and first[i+1][j].flag == False: # checks that the square hasn't already been selected or flagged
            first[i+1][j].visible = True # check the value of the square
            if first[i+1][j].val==0: # if it is zero, clear it automatically
                open_game(first,first[i+1][j])
    # This process repeats for the directions up, down, left ,right, up-right, down-right, up-left, and down-left

        if j+1 < len(first):
            if first[i+1][j+1].visible == False and first[i+1][j+1].flag == False:
                first[i+1][j+1].visible = True
                if first[i+1][j+1].val == 0:
                    open_game(first,first[i+1][j+1])

        if j-1 >= 0:
            if first[i+1][j-1].visible == False and first[i+1][j-1].flag == False:
                first[i+1][j-1].visible = True
                if first[i+1][j-1].val == 0:
                    open_game(first,first[i+1][j-1])
    if i - 1>= 0:
        if first[i-1][j].visible == False and first[i-1][j].flag == False:
            first[i-1][j].visible = True
            if first[i-1][j].val == 0:
                open_game(first, first[i-1][j])
        if j+1 < len(first):
            if first[i-1][j+1].visible == False and first[i-1][j+1].flag == False:
                first[i-1][j+1].visible = True
                if first[i-1][j+1].val == 0:
                    open_game(first, first[i-1][j+1])
        if j-1>= 0:
            if first[i-1][j-1].visible == False and first[i-1][j-1].flag == False:
                first[i-1][j-1].visible = True
                if first[i-1][j-1].val == 0:
                    open_game(first,first[i-1][j-1])
    if j-1 >= 0:
        if first[i][j-1].visible == False and first[i][j-1].flag == False:
            first[i][j-1].visible = True
            if first[i][j-1].val == 0:
                open_game(first,first[i][j-1])
    if j+1 < len(first):
        if first[i][j+1].visible == False and first[i][j+1].flag == False:
            first[i][j+1].visible = True
            if first[i][j+1].val == 0:
                open_game(first, first[i][j+1])
            

def game(n, bombs):
    grey = pygame.image.load('grey!!.png') # 40x40 pixel image for the grey squares
    white = pygame.image.load('white!.png') # 40x40 for the exposed white space
    zero = pygame.image.load('zero!.png') # all the following are 20x20 pixels 
    one = pygame.image.load('one!.png')
    two = pygame.image.load('two!.png')
    three = pygame.image.load('three!.png')
    four = pygame.image.load('four!.png')
    five = pygame.image.load('five!.png')
    six = pygame.image.load('six!.png')
    seven = pygame.image.load('seven!.png')
    eight = pygame.image.load('eight!.png')
    nine = pygame.image.load('mine!.jpg')
    flag = pygame.image.load('flag!.jpg')

    numbers = [zero,one,two,three,four,five,six,seven,eight,nine] # orders the loaded images into a list to be called later
    table = minesweeper(n,bombs) # creates the table of values
    c = Board(table) # creates the gameboard from the table
    w = h = len(c.board)*40 # sets the wwidth and height for the game window,
    # it has to be proportional to the gameboard, and since the squares are 40x40 p, we multiply that by the number of squares.
    screen = pygame.display.set_mode((w,h))

    fclick = False
    # Makes a list of the squares as a board and displays the initial board (just grey images)
    first = [[] for i in range(n)]
    for i in range(0,n*40,40): # Again, each square is 40x40 pixels
        for j in range (0,n*40,40):
            first[i//40] += [Square(i,j,40,40,c.board,(i//40,j//40))]
            screen.blit(grey,(i,j))

    run = True
    start = time.time() # begins the game timer
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN: # If the user presses 'r' the game restarts
                if event.key == pygame.K_r:
                    run = False
                    restart(n,bombs)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # If the user left clicks
                    for i in first:
                        for j in i:
                            mouse = pygame.mouse.get_pos()
                            r = pygame.rect.Rect(mouse,(1,1))
                            if j.rect.colliderect(r):
                                if fclick:
                                    if j.flag == False: # if the tile left-clicked isn't flagged 
                                        if j.val == 9: # if the tile left-clicked is a bomb
                                            print('LOSER')
                                            run = False # ends the game
                                        
                                        j.visible = True # makes the value of the square visible
                                        if j.val == 0: # if the selected square is not touching any bombs
                                            j.visible = open_game(first,j) # clear the surrounding zero squares automatically
                                            j.visible = True
                                else: #This ensures that the first square selected in the game is a zero square (so you can't immediately lose)
                                    goodset = False # event that indicates if the first square pressed equals zero
                                    while not goodset: # recreates the board if the selected square is not zero
                                        table = minesweeper(n,bombs)
                                        c = Board(table)
                                        first = [[] for i in range(n)]
                                        for i in range(0,n*40,40):
                                            for j in range (0,n*40,40):
                                                first[i//40] += [Square(i,j,40,40,c.board,(i//40,j//40))]
                                                screen.blit(grey,(i,j))
                                        for x in first:
                                            for y in x:
                                                r = pygame.rect.Rect(mouse,(1,1))
                                                if y.rect.colliderect(r):
                                                    if y.val == 0:
                                                        goodset = True # if the selected square is zero, we are set to go through the rest of the game
                                                        fclick = True
                                                        
                                                        y.visible = open_game(first,y) # auto-clear surrounding zeros
                                                        y.visible = True
                                    
                                    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #if the user right-clicks
                 for i in first:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                            if j.rect.colliderect(r):
                                if j.visible == False: # if the square hasn't been chosen already
                                    if j.flag == False: # if there is not already a flag
                                       j.flag = True # place the flag
                                    elif j.flag == True: #remove the flag if there is already one placed
                                       j.flag = False
        # Update display as the user plays                            
        for i in first:
            for j in i:
                if j.visible == True:
                    screen.blit(white, (j.x,j.y)) # display the white square
                    screen.blit(numbers[j.val],(j.x + 10,j.y+10)) # display the correct number over the white (adding 10 to center the images on the square)
                if j.flag == True:
                    screen.blit(flag,(j.x+10,j.y+10)) # display the flag
                if j.flag == False and j.visible == False: # if the square has not been pressed yet, remain grey
                    screen.blit(grey, (j.x,j.y))
        # Determine whether the user has won yet or not
        count = 0 # count for the number of squares made visible (left-clicked by user)
        for i in first:
            for j in i:
                if j.visible == True and j.val != 9: #if the square has been left-clicked and it's not a bomb
                    count += 1 # add it to the count
            if count == (n*n)- bombs:
                run = False # end the game
                print('Congrats you win!')
                end = time.time() # stop the timer
                print('Time:',round(end-start,2),'s') # displays time in seconds
                print(round((end-start)/60,2), 'min') # time in minutes
        pygame.display.update()

    for i in first:
        for j in i:
            if j.val == 9:
                screen.blit(nine, (j.x+10,j.y+10))
    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    restart(n,bombs)
print('Welcome to Minesweeper!')
print('press "r" to restart a game')
print('The table will be n x n tiles.')
n = int(input('Please enter the n of the table: ')) # get the size of the board
# Determine how many bombs will be placed on the board depending on user preference
easy = (n*n)//9 # few bombs
medium = (n*n)//6 
hard = (n*n)//4 # lots of bombs
diff = 0
while diff != 'e' and diff != 'm' and diff != 'h':
    diff = input('easy (e), medium (m), or hard (h)?: ')
    if not diff:
        diff = 0
        print('please try again')
    elif diff[0] == 'e':
        bombs = easy
    elif diff[0] == 'm':
        bombs = medium
    elif diff[0] == 'h':
        bombs = hard
    else:
        print('please try again')
game(n,bombs) # run the game!
         

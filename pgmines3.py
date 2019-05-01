from random import randint
import pygame
import time
pygame.init()

def minesweeper(n,bombs):
    table = make_table(n)
    table = add_bombs(table,bombs)
    table = change_table(table)
    return table

def make_table(n):
    return [[0]*n for i in range(n)]

def add_bombs(table,bombs):
    for i in range(bombs):
        is_bomb = False
        while not is_bomb:
            x = randint(0, len(table) - 1)
            y = randint(0, len(table) - 1)
            if table[x][y] != 9:
                table[x][y] = 9
                is_bomb = True
    return table

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

def check_down_right(table,x,y):
    if x + 1 < len(table[x]) and y - 1>= 0:
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

def pr(table):
    for i in table:
        print (i)

class Board:
    def __init__(self,board):
        self.board = board
    def __repr__(self):
        pr(self.board)
        
        return "is your table"

class Square:
    def __init__(self,x,y,w,h,board,ij):
        self.rect = pygame.rect.Rect(x,y,w,h)
        i,j = ij
        self.val = board[i][j]
        self.x = x
        self.y = y
        self.visible = False
        self.flag = False

def restart(n,bombs):
    game(n,bombs)

def open_game(first, square):
    square.visible = True
    i,j = square.x//40,square.y//40
    if i + 1 < len(first):
        if first[i+1][j].visible == False and first[i+1][j].flag == False:
            first[i+1][j].visible = True
            if first[i+1][j].val==0:
                open_game(first,first[i+1][j])

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
    grey = pygame.image.load('grey!!.png')
    white = pygame.image.load('white!.png')
    zero = pygame.image.load('zero!.png')
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

    numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
    table = minesweeper(n,bombs)
    c = Board(table)
    w = h = len(c.board)*40
    screen = pygame.display.set_mode((w,h))

    fclick = False
    first = [[] for i in range(n)]
    for i in range(0,n*40,40):
        for j in range (0,n*40,40):
            first[i//40] += [Square(i,j,40,40,c.board,(i//40,j//40))]
            screen.blit(grey,(i,j))

    run = True
    start = time.time()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    restart(n,bombs)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in first:
                        for j in i:
                            mouse = pygame.mouse.get_pos()
                            r = pygame.rect.Rect(mouse,(1,1))
                            if j.rect.colliderect(r):
                                if fclick:
                                    if j.flag == False:
                                        if j.val == 9:
                                            print('LOSER')
                                            run = False
                                        
                                        j.visible = True
                                        if j.val == 0:
                                            j.visible = open_game(first,j)
                                            j.visible = True
                                else:
                                    goodset = False
                                    while not goodset:
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
                                                        goodset = True
                                                        fclick = True
                                                        
                                                        y.visible = open_game(first,y)
                                                        y.visible = True
                                    
                                    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                 for i in first:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                            if j.rect.colliderect(r):
                                if j.visible == False:
                                    if j.flag == False:
                                       j.flag = True
                                    elif j.flag == True:
                                       j.flag = False
                                    
        for i in first:
            for j in i:
                if j.visible == True:
                    screen.blit(white, (j.x,j.y))
                    screen.blit(numbers[j.val],(j.x + 10,j.y+10))
                if j.flag == True:
                    screen.blit(flag,(j.x+10,j.y+10))
                if j.flag == False and j.visible == False:
                    screen.blit(grey, (j.x,j.y))
        count = 0
        for i in first:
            for j in i:
                if j.visible == True and j.val != 9:
                    count += 1
            if count == (n*n)-bombs:
                run = False
                print('Congrats you win!')
                end = time.time()
                print('Time:',round(end-start,2),'s')
                print(round((end-start)/60,2), 'min')
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
n = int(input('Please enter the n of the table: '))
easy = (n*n)//9
medium = (n*n)//6
hard = (n*n)//4
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
game(n,bombs)
         

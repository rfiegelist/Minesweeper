from random import randint
import pygame
pygame.init()

def mine(n,bombs):
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

def check_down_left(table,x,y):
    if x + 1 < len(table[x]) and y - 1>= 0:
        if table[x+1][y-1] != 9:
            table[x+1][y-1] += 1
    return table

def check_down_right(table,x,y):
    if x + 1 < len(table[0]) and y + 1 < len(table):
        if table[x+1][y+1] != 9:
            table[x+1][y+1] += 1
    return table

def check_down(table,x,y):
    if x + 1 < len(table[0]):
        if table[x+1][y] != 9:
            table[x+1][y] += 1
    return table

def check_up_left(table,x,y):
    if x - 1 >= 0 and y - 1 >= 0:
        if table[x-1][y-1] != 9:
            table[x-1][y-1] += 1
    return table

def check_up_right(table,x,y):
    if x - 1 >= 0 and y + 1 < len(table):
        if table[x-1][y+1] != 9:
            table[x-1][y+1] += 1
    return table

def check_up(table,x,y):
    if x - 1 >= 0:
        if table[x-1][y] != 9:
            table[x-1][y] += 1
    return table

def check_left(table,x,y):
    if y - 1 >= 0:
        if table[x][y-1] != 9:
            table[x][y-1] += 1
    return table

def check_right(table,x,y):
    if y + 1 < len(table):
        if table[x][y+1] != 9:
            table[x][y+1] += 1
    return table

def pr(table):
    for i in table:
        print (i)

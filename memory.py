from random import *
from collections import *
import time
#import PySimpleGUI as sg
import io
import os
from PIL import Image
from os import path 

def print_board(board: list[list[int]], rows: int, cols: int):
    for i in range (0, rows):
            print(board[i])
    return 
def initialize_board(board: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    for i in range (0, rows):
        for j in range(0, cols):
            board[i][j] = -1
    return board
def check_board(board: list[list[int]], number: int) -> bool:
    sum = 0
    for i in range (0, len(board[0]) ):
        
        sum += board[i].count(number)
        #print(sum)
    if sum <= 1:
        return True
    return False
# def create_layout(layout: list[list[int]], board: list[list[int]], level: int, flag: bool) -> list[list[int]]:
#         newNum = 0
#         count = 0
#         for i in range(0,(level * 2)):
#             for j in range(0,(level * 2)):
#                 layout[i][j] = sg.Button(str(board[i][j]))
#         if flag == True:
#             layout[0][0] = sg.Button("End Round")            
        
#         return layout
def create_board(board: list[list[int]],  level: int, size: int) -> list[list[int]]:
        newNum = 0
        count = 0
        for i in range(0,(level * 2)):
            for j in range(0,(level * 2)):
                #print("i is:" + str(i))
                #print("j is:" + str(j))
                while(count < size):
                    newNum = randrange(0,(size / 2))
                    #print("new num is: " + str(newNum))
                    if check_board(board, newNum) == True:
                        board[i][j] = newNum
                        count += 1
                        #print("NewNumer is" + str(newNum))
                        break
                        
        
        return board
def run_game(board: list[list[int]], level: int, rows: int, cols: int, choice1_row: int, choice1_col: int, choice2_row: int, choice2_col: int) -> bool:
    if choice1_row == choice2_row and choice1_col == choice2_col:
        print("You cannot select that same element twice! Try Again")
        return False
    try:
        if board[int(choice1_row) - 1][int(choice1_col) - 1] == board[int(choice2_row) - 1][int(choice2_col) - 1]:
            return True
        return False
    except IndexError:
        print("Invalid Entries. Please Try again!")
        return False
def open_picture(board: list[list[int]], row: int, col: int):
    Cow = r"C:\Users\Parker\Pictures\cow.jpg"
    Pig = r"C:\Users\Parker\Pictures\pig.jpg"
    Fox = r"C:\Users\Parker\Pictures\fox.jpg"
    Squirrel = r"C:\Users\Parker\Pictures\Squirrel.jpg"
    Frog = r"C:\Users\Parker\Pictures\frog.jpg"
    Cat = r"C:\Users\Parker\Pictures\cat.jpg"
    Chicken = r"C:\Users\Parker\Pictures\Chicken.jpg"
    Rabbit = r"C:\Users\Parker\Pictures\rabbit.jpg"
    Buttefly = r"C:\Users\Parker\Pictures\butterfly.jpg.jpg"
    try:
        if board[int(row) - 1][int(col) - 1] == 0:
            return Image.open(Cow, 'r')
        if board[int(row) - 1][int(col) - 1] == 1:
            return Image.open(Pig, 'r')
        if board[int(row) - 1][int(col) - 1] == 2:
            return Image.open(Fox, 'r')
        if board[int(row) - 1][int(col) - 1] == 3:
            return Image.open(Squirrel, 'r')
        if board[int(row) - 1][int(col) - 1] == 4:
            return Image.open(Frog, 'r')
        if board[int(row) - 1][int(col) - 1] == 5:
            return Image.open(Cat, 'r')
        if board[int(row) - 1][int(col) - 1] == 6:
            return Image.open(Chicken, 'r')
        if board[int(row) - 1][int(col) - 1] == 7:
            return Image.open(Buttefly, 'r')
        if board[int(row) - 1][int(col) - 1] == 8:
            return Image.open(Rabbit, 'r')
    except IndexError:
        print("Invalid Entries. Please Try again!")
        return None
    return None
        
        


def prompt_user(board: list[list[int]], level: int, rows: int, cols: int):
    choice2_col = 0
    choice2_row = 0
    choice1_col = 0
    choice1_row = 0
    result = False
    count = 0
    score = 0
    end_game = (rows * cols) / 2
    user_board = [[0 for i in range(cols)] for j in range(rows)]
    for a in range(0,(level * 2)):
        for b in range(0,(level * 2)):
            user_board[a][b] = count
            count += 1
    while True:
        

        
        print_board(user_board, rows, cols)
        print("Above are the options for choices in our matching game. Select two choices to see if they are matches")
        print("Selections are made by row and column. For example to choose option 0, input row 1, column 1")
        print("Matched cards will be represented by a -1 so you do not select them again!")
        choice1_row = input("First Choice row number: ")
        choice1_col = input("First Choice Column number: ")
        try:
            file1 = open_picture(board, choice1_row, choice1_col)
            file1.show()
            file1.close()
           
        except AttributeError:
            print("Image does not exsit")
        choice2_row = input("Second Choice row number: ")
        choice2_col = input("Second Choice Column number: ")
        try:
            file2 = open_picture(board, choice2_row, choice2_col)
            file2.show()
            time.sleep(2)
            file2.close()
        except AttributeError:
            print("Image does not exsit")
             
        # try:
        #     file1.close()
        #     file2.close()
        # except AttributeError:
        #     print("Image does not exsit")
        os.system("TASKKILL /F /IM Microsoft.Photos.exe")
        result = run_game(board, level, rows, cols, choice1_row, choice1_col, choice2_row, choice2_col)
        if result == True:
            print("Thats a match!")
            score += 1
            user_board[int(choice1_row) - 1][int(choice1_col) - 1] = -1
            user_board[int(choice2_row) - 1][int(choice2_col) - 1] = -1
        else:
            print("Thats not a match!")
        if score == end_game:
            if level != 4:
                print("You got them all! Onto the next level!")
                break
            else:
                print("Congrats! You've beaten all of the levels")
                break


        
class Solution(object):
    
    def main():
        
        level = 1
        for level in range (1, 4):
            rows, cols = ((level * 2), (level * 2))
            size = rows * cols
            board = [[0 for i in range(cols)] for j in range(rows)]
            #layout = [[0 for i in range(cols)] for j in range(rows)]
            board = initialize_board(board, rows, cols)
            
            board = create_board(board, level, size)
           
            #layout = create_layout(layout, board, level, False)
            #print("NEW BOARD__________________________________________")
            #print_board(board, rows, cols)
          
            prompt_user(board, level, rows, cols,)
            
            sum = 0




























        # sg.theme('Dark Blue 3')  # please make your windows colorful
        # window = sg.Window("Memory Game", layout, margins = (500, 100))
        # while True:
        #     event, values = window.read()
        #     while sum <= 4:
        #         event, values = window.read()
        #         if event == "0" or event == "1" or event == "2":
        #             print("GOOD ENTRY")
        #             sum += 1
        #         if sum >= 3:
        #             layout = create_layout(layout, board, level, True)
        #             window = sg.Window("Memory Game", layout, margins = (500, 100))
        #             break
        #     if event == "End Round" or event == sg.WIN_CLOSED:
        #         break

        # window.close()
            
            

    main()
    #

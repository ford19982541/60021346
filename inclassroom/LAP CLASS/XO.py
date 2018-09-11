#you need to have a X.png 100*100
#you need to have a O.png 100*100
#you need to have a E.png 100*100 for background any color you like



Turn = "X"
clicked_home = []
list_x = []
list_o = []
wintime_player1 = 0
wintime_player2 = 0
player1 = "Player1"
player2 = "Player2"
from tkinter import *
from tkinter import ttk,messagebox
from tkinter import messagebox
import sys
import tkinter
Game = True
def main():
        global Turn, wintime_player1 , wintime_player2 , Game
        global Game
        root = Tk()
        root.resizable(False , False)
        root.title("X O")
        root.config(background = "peach puff")
        image_x = PhotoImage(file = "X.png")
        image_o = PhotoImage(file = "O.png")
        empty = PhotoImage(file = "E.png")

        lplayer1 = Label (root , text = (wintime_player1 , ":" , player1) , background = "peach puff")
        lplayer2 = Label (root , text = (wintime_player2, ":" , player2) , background = "peach puff")
        l1 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l1.bind("<1>" , lambda e : click_home(l1 , 1))
        l2 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l2.bind("<1>" , lambda e : click_home(l2 , 2))
        l3 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l3.bind("<1>" , lambda e : click_home(l3 , 3))
        l4 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l4.bind("<1>" , lambda e : click_home(l4 , 4))
        l5 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l5.bind("<1>" , lambda e : click_home(l5 , 5))
        l6 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l6.bind("<1>" , lambda e : click_home(l6 , 6))
        l7 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l7.bind("<1>" , lambda e : click_home(l7 , 7))
        l8 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l8.bind("<1>" , lambda e : click_home(l8 , 8))
        l9 = Label (root , background = "navy" , relief = SUNKEN , image = empty)
        l9.bind("<1>" , lambda e : click_home(l9 , 9))
        lturn = Label(root , text = ("Turn : "+Turn)  , background = "peach puff")
        ###################
        def click_home(label , number):
                global Game , Turn , list_x , list_o , wintime_player1 , wintime_player2
                if label in clicked_home : pass
                elif Game == True:
                        clicked_home.append(label)
                        global Turn , list_x , list_o
                        if Turn == "X":
                                label.config(image = image_x)
                                Turn = "O"
                                list_x.append(number)
                        else:
                                label.config(image = image_o)
                                Turn = "X"
                                list_o.append(number)
                        lturn.config(text = "Turn : " + Turn)
                if 1 in list_x and 2 in list_x and 3 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 1 in list_o and 2 in list_o and 3 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = tkmessageox.askyesno("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 4 in list_x and 5 in list_x and 6 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 4 in list_o and 5 in list_o and 6 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 7 in list_x and 8 in list_x and 9 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 7 in list_o and 8 in list_o and 9 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 1 in list_x and 4 in list_x and 7 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 1 in list_o and 4 in list_o and 7 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 2 in list_x and 5 in list_x and 8 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 2 in list_o and 5 in list_o and 8 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 3 in list_x and 6 in list_x and 9 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 3 in list_o and 6 in list_o and 9 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 1 in list_x and 5 in list_x and 9 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 1 in list_o and 5 in list_o and 9 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 3 in list_x and 5 in list_x and 7 in list_x:
                        wintime_player1 += 1
                        lplayer1.config(text = (wintime_player1 , ":" , player1) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()
                elif 3 in list_o and 5 in list_o and 7 in list_o:
                        wintime_player2 += 1
                        lplayer2.config(text = (wintime_player2 , ":" , player2) )
                        Game = False
                        result = messagebox.askokcancel("NewGame","Would you like to play again?")
                        if result == True:
                                dnew_game()
                        elif result==False:
                                exit()

        def dnew_game():
                global Game , list_x , list_o , clicked_home , Turn
                Game = True
                l1.config(image = empty)
                l2.config(image = empty)
                l3.config(image = empty)
                l4.config(image = empty)
                l5.config(image = empty)
                l6.config(image = empty)
                l7.config(image = empty)
                l8.config(image = empty)
                l9.config(image = empty)
                del clicked_home
                clicked_home = []
                del list_x
                list_x = [ ]
                del list_o
                list_o = [ ]
        bnew_game = Button (root , text = "New Game!" , command = lambda : dnew_game() , background = "lemon chiffon")
        lturn.grid(row = 0 , column = 0 , sticky = W)
        bnew_game.grid(row = 1 , column = 0  , sticky = W)
        lplayer1.grid(row = 0 , column = 2 , sticky = E)
        lplayer2.grid(row = 1 , column = 2 , sticky = E)
        l1.grid(row = 2 , column = 0)
        l2.grid(row = 2 , column = 1)
        l3.grid(row = 2 , column = 2)
        l4.grid(row = 3 , column = 0)
        l5.grid(row = 3 , column = 1)
        l6.grid(row = 3 , column = 2)
        l7.grid(row = 4 , column = 0)
        l8.grid(row = 4 , column = 1)
        l9.grid(row = 4 , column = 2)
        root.mainloop()
main()

from tkinter import *
from string import Template
import random
import math
def next_turn(row,col):
   global player
   if game_buttens[row][col]['text']==""and check_winner()==False:
       if player==players[0]:
           game_buttens[row][col]['text']=player
           if check_winner()==False:
               player=players[1]
               label.config(text=(players[1] +" turn"))
           elif check_winner()==True:
               label.config(text=(players[0] +" wins!")) 
           elif check_winner()=='tie':
               label.config(text=("Tie,no one wins!"))
       elif player==players[1]:
        game_buttens[row][col]['text']=player
        if check_winner()==False:
            player=players[0]
            label.config(text=(players[0] +" turn"))
        elif check_winner()==True:
            label.config(text=(players[1] +" wins!")) 
        elif check_winner()=='tie':
            label.config(text=("Tie,no one wins!"))            
def check_winner():
    for row in range(3):
        if game_buttens[row][0]['text']==game_buttens[row][1]['text']==game_buttens[row][2]['text']!="":
            game_buttens[row][0].config(text="",bg='green')
            game_buttens[row][1].config(text="",bg='green')
            game_buttens[row][2].config(text="",bg='green')
            return True
    for col in range(3):
       if game_buttens[0][col]['text']==game_buttens[1][col]['text']==game_buttens[2][col]['text']!="":
           game_buttens[0][col].config(text="",bg='green')
           game_buttens[1][col].config(text="",bg='green')
           game_buttens[2][col].config(text="",bg='green')
           return True
       
    if game_buttens[0][0]['text']==game_buttens[1][1]['text']==game_buttens[2][2]['text']!="":
         game_buttens[0][0].config(text="",bg='green')
         game_buttens[1][1].config(text="",bg='green')
         game_buttens[2][2].config(text="",bg='green')
         return True   
    elif game_buttens[0][2]['text']==game_buttens[1][1]['text']==game_buttens[2][0]['text']!="":
         game_buttens[2][0].config(text="",bg='green')
         game_buttens[1][1].config(text="",bg='green')
         game_buttens[0][2].config(text="",bg='green')
         return True 
    if check_empty() ==False:
        for row in range(3):
            for col in range((3)):
                game_buttens[row][col].config(bg='red')
        return 'tie'
    else :
        return False
def check_empty():
    spases=9
    for row in range(3):
        for col in range(3):
            if game_buttens[row][col]['text']!="":
                spases-=1
                
    if spases==0:
        return False 
    else:
        return True
def start_new_game():
    global player
    player=random.choice(players)
    label.config(text=(player+"turn"))
    for row in range(3):
        for col in range(3):
            game_buttens[row][col].config(text="",bg='white')


window=Tk()
window.title("Tic Tac Toe")
players=["X","O"]
player=random.choice(players)
game_buttens=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
label=Label(text=(player+" turn"),font=('consolas',40))
label.pack(side="top")

restart_button=Button(text="restart",font=('consolas',20),command=start_new_game)

restart_button.pack(side="top")  
buttens_frame=Frame(window)
buttens_frame.pack()
for  row in range(3):
    for col in range(3):
        game_buttens[row][col]=Button(buttens_frame,text="",font=('consolas',50),width=4,height=1,
                                      command=lambda row=row,col=col:next_turn(row, col))
        game_buttens[row][col].grid(row=row,column=col)
        
 
window.mainloop()    


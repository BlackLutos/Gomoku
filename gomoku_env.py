import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import tkinter.simpledialog as sd
import numpy as np


class Gomoku(tk.Tk, object):
    def __init__(self, size=15):
        super(Gomoku, self).__init__()
        self.size = size
        self.title('Gomoku')
        self.iconbitmap('icon.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 3
        y = (screen_height - self.winfo_height()) // 4
        self.geometry('{0}x{1}+{2}+{3}'.format(510, self.size*30, x, y))
        player_choose = tkinter.messagebox.askquestion("Choose Color", "Choose your chess color:\nYes: Black\nNo: White")
        if player_choose == 'yes':
            self.current_player = 'black'
        else:
            self.current_player = 'white'
        self.current_chessboard = np.zeros((size, size))
        self.build_chessboard()
        self.player()

    def build_chessboard(self):
        self.canvas = tk.Canvas(self, bg='#f9d65b', height=self.size*30, width=self.size*35)

        for i in range(self.size):
            self.canvas.create_line(15+i*30, 15, 15+i*30, 435)
            self.canvas.create_line(15, 15+i*30, 435, 15+i*30)
            self.canvas.create_text(15+i*30, 1, text=str(i), anchor='n')
            self.canvas.create_text(1, 8+i*30, text=str(i), anchor='nw')
        
        self.canvas.create_text(500, 90, text='Take turns:', anchor='e')
        self.canvas.create_text(503, 120, text=self.current_player + ' chess', anchor='e', tags='player_text')

        self.canvas.pack()

        style = ttk.Style()
        # print(style.theme_names())
        style.configure('my.TButton', font=('Helvetica', 7), foreground='black')

        reset_btn = ttk.Button(self.canvas,text="Restart", command=self.reset, style='my.TButton')
        reset_btn.place(x=440, y=400)

    def update_text(self, current_player):
        self.canvas.delete('player_text')
        self.canvas.create_text(503, 120, text=self.current_player + ' chess', anchor='e', tags='player_text')

    def black(self,event):
        self.draw_chess(event.x//30, event.y//30, 'black')


    def white(self,event):
        self.draw_chess(event.x//30, event.y//30, 'white')

    def player(self):
        if self.current_player == 'black':
            self.canvas.bind('<Button-1>', self.black)
            self.current_player = 'white'

        elif self.current_player == 'white':
            self.canvas.bind('<Button-1>', self.white)
            self.current_player = 'black'

    def judge_win(self, current_chessboard):
        chb = current_chessboard
        if self.current_player == 'white':
            for i in range(self.size):
                for j in range(self.size -4):
                    if chb[i][j] == 1 and chb[i][j+1] == 1 and chb[i][j+2] == 1 and chb[i][j+3] == 1 and chb[i][j+4] == 1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(self.size):
                    if chb[i][j] == 1 and chb[i+1][j] == 1 and chb[i+2][j] == 1 and chb[i+3][j] == 1 and chb[i+4][j] == 1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(self.size -4):
                    if chb[i][j] == 1 and chb[i+1][j+1] == 1 and chb[i+2][j+2] == 1 and chb[i+3][j+3] == 1 and chb[i+4][j+4] == 1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(4, self.size):
                    if chb[i][j] == 1 and chb[i+1][j-1] == 1 and chb[i+2][j-2] == 1 and chb[i+3][j-3] == 1 and chb[i+4][j-4] == 1:
                        self.show_win(self.current_player)

        elif self.current_player == 'black':
            for i in range(self.size):
                for j in range(self.size -4):
                    if chb[i][j] == -1 and chb[i][j+1] == -1 and chb[i][j+2] == -1 and chb[i][j+3] == -1 and chb[i][j+4] == -1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(self.size):
                    if chb[i][j] == -1 and chb[i+1][j] == -1 and chb[i+2][j] == -1 and chb[i+3][j] == -1 and chb[i+4][j] == -1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(self.size -4):
                    if chb[i][j] == -1 and chb[i+1][j+1] == -1 and chb[i+2][j+2] == -1 and chb[i+3][j+3] == -1 and chb[i+4][j+4] == -1:
                        self.show_win(self.current_player)
            for i in range(self.size -4):
                for j in range(4, self.size):
                    if chb[i][j] == -1 and chb[i+1][j-1] == -1 and chb[i+2][j-2] == -1 and chb[i+3][j-3] == -1 and chb[i+4][j-4] == -1:
                        self.show_win(self.current_player)

                   
                        
                        
    def show_win(self, current_player):
        if current_player == 'black':
            print('White win')
            tkinter.messagebox.showinfo(title='Game Over', message='White chess win ! \nRestart Game.')
            self.reset()

        elif current_player == 'white':
            print('black win')
            reply = tkinter.messagebox.showinfo(title='Game Over', message='Black chess win ! \nRestart Game.')
            self.reset()


    def draw_chess(self, x, y, color):
        old_x = x
        old_y = y
        x = 15 + x*30
        y = 15 + y*30
        if self.current_chessboard[old_y][old_x] == 0:
            self.canvas.create_oval(x-13, y-13, x+13, y+13, fill=color, tags='chess')
            self.current_chessboard[old_y][old_x] = 1 if color == 'black' else -1
        else:
            if self.current_player == 'black':
                self.current_player = 'white'
            elif self.current_player == 'white':
                self.current_player = 'black'
        self.judge_win(self.current_chessboard)
        if self.current_player == 'black':
            print(self.current_chessboard, 'white', '\n')
        elif self.current_player == 'white':
            print(self.current_chessboard, 'black', '\n')     
        self.update_text(self.current_player)   
        self.player()

    def reset(self):
        self.update()
        self.canvas.delete('chess')
        self.current_chessboard = np.zeros((self.size, self.size))
        self.current_player = 'black'

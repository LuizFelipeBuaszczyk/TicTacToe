from ctypes import c_char
from tkinter import Button, Frame

from settings import TICTACTOE_LIB

current_player = 'X'

class Actions:

    @staticmethod
    def play(x: int, y: int, button: Button) -> None:
        global current_player
        
        if (TICTACTOE_LIB.play(x,y) > 0):
            raise Exception("Jogada Inválida")


        button.config(text=current_player)
        
        TICTACTOE_LIB.check_winner.argtypes = [c_char]
        print(TICTACTOE_LIB.check_winner(current_player.encode('utf-8')))
        current_player = 'O' if current_player == 'X' else 'X'

    @staticmethod
    def start_game(gameboard_frame: Frame) -> None:
        TICTACTOE_LIB.start_game()    
    
        global current_player 
        current_player = 'X'
        
        for value in gameboard_frame.children.values():
            if isinstance(value, Button):
                value.config(text='')

        gameboard_frame.pack()

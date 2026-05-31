from tkinter import Button, Frame

current_player = 'X'

class Actions:

    @staticmethod
    def play(x: int, y: int, button: Button) -> None:
        global current_player

        button.config(text=current_player)
        current_player = 'O' if current_player == 'X' else 'X'

    @staticmethod
    def start_game(gameboard_frame: Frame) -> None:
        global current_player 
        current_player = 'X'

        for value in gameboard_frame.children.values():
            if isinstance(value, Button):
                value.config(text='')

        gameboard_frame.pack()

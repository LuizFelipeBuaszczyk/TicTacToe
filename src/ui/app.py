import tkinter as tk

from ui.actions import Actions

class Application:

    def __init__(self, master: tk.Tk) -> None:
        self.frame = tk.Frame(master)
        self.frame.pack(side="top")
        
        self._load_header(master)
        self.gameboard = self._load_gameboard()
        self._load_action_button()
    
    def _load_header(self, master: tk.Tk) -> None:
        header = tk.Frame(self.frame)
        header.pack()

        tk.Label(header, text="Jogo da Velha").pack(side="left")
        tk.Button(header, text="Quit", command=master.destroy).pack(side="left")

    def _load_action_button(self) -> None:
        action_buttons = tk.Frame(self.frame)
        action_buttons.pack()

        tk.Button(action_buttons, text="Jogar", command=lambda gameboard=self.gameboard: Actions.start_game(gameboard)).pack(side="left")

    def _load_gameboard(self) -> tk.Frame:
        gameboard = tk.Frame(self.frame)
        
        for i in range(3):
            for j in range(3):
                button: tk.Button | None = tk.Button(
                    gameboard,
                    text=""  
                ) 
                button.config(command=lambda row=i, column=j, btn=button: Actions.play(row, column, btn))

                button.grid(row=i, column=j)

        return gameboard



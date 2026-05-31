from tkinter import Tk
from ui.app import Application
from utils import get_central_point

WIDTH = 800
HEIGHT = 600
X, Y = get_central_point(WIDTH, HEIGHT)

SCREEN_RESOLTION = f"{WIDTH}x{HEIGHT}+{X}+{Y}"


root = Tk()
root.geometry(SCREEN_RESOLTION)


Application(root)
root.mainloop()

import View.main as GUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI.GUI(root)
    app.pack()
    root.mainloop()


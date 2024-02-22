import tkinter as tk

class BattleScreen(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        
        self.buttons = [[None] * 7 for _ in range(7)]
        img = tk.PhotoImage(width=1, height=1)

        for row in range(7):
            for col in range(7):
                button = tk.Button(self, image=img, compound='c', width=100, height=100, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        print(f"Button clicked at row {row}, column {col}")

class Controls(tk.Frame):
    def __init__(self, root, battle_screen):
        tk.Frame.__init__(self, root)

        self.battle_screen = battle_screen

        self.quit_button = tk.Button(self, text="Quit", width=6, command=root.destroy)
        self.quit_button.pack()

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("7x7 Game")

        self.battle_screen = BattleScreen(self.root)
        self.battle_screen.pack()

        self.controls = Controls(self.root, self.battle_screen)
        self.controls.pack()

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
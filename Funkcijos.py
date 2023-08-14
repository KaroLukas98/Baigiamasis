from tkinter import *
import random


class TicTacToeGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.players = ["X", "O"]
        self.player = self.players[0]

        self.buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.create_board_widgets()

        self.label = Label(text=self.player + " eilė", font=('consolas', 40))
        self.label.pack(side="top")

        self.reset_button = Button(text="Restart", font=('consolas', 20), command=self.new_game)
        self.reset_button.pack(side="top")

        self.create_menu()
        self.computer_playing = False

    def create_menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        game_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Meniu", menu=game_menu)
        game_menu.add_command(label="Naujas žaidimas", command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Žaisti su kompiuteriu", command=self.start_computer_game)
        game_menu.add_separator()
        game_menu.add_command(label="Išeiti", command=self.window.quit)

    def computer_move(self):
        if self.computer_playing and not self.check_winner() and self.empty_spaces() and self.player == "O":
            empty_cells = [(row, col) for row in range(3) for col in range(3) if self.buttons[row][col]['text'] == ""]
            if empty_cells:
                random_row, random_col = random.choice(empty_cells)
                self.next_turn(random_row, random_col)

    def start_computer_game(self):
        self.reset_game()
        self.player = self.players[random.randint(0, 1)]
        self.label.config(text=self.player + " eilė")
        self.computer_playing = True
        self.computer_move()

    def reset_game(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " eilė")

    def create_board_widgets(self):
        frame = Frame(self.window)
        frame.pack()

        for row in range(3):
            for column in range(3):
                button = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                command=lambda row=row, column=column: self.next_turn(row, column))
                button.grid(row=row, column=column)
                self.buttons[row][column] = button

    def check_tie(self):
        if self.empty_spaces():
            return False
        elif self.check_winner():
            return False
        else:
            return True

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():

            self.buttons[row][column]['text'] = self.player

            if self.check_winner():
                self.label.config(text=self.player + " Laimėjo")
            elif self.check_tie():
                self.label.config(text="Lygiosios!")
            else:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=self.player + " Eilė")
                if self.computer_playing and self.player == "O":
                    self.computer_move()
        elif self.check_tie():
            self.label.config(text="Lygiosios!")

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.buttons[row][0].config(bg="green")
                self.buttons[row][1].config(bg="green")
                self.buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column].config(bg="green")
                self.buttons[1][column].config(bg="green")
                self.buttons[2][column].config(bg="green")
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][2].config(bg="green")
            return True

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][0].config(bg="green")
            return True

    def empty_spaces(self):
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] == "":
                    return True
        return False

    def new_game(self):
        self.computer_playing = False
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " eilė")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")

    def run(self):
        self.window.mainloop()

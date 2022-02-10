import MenaceAI.MenaceCore as Menace
import tkinter as tk
import time


class BadMove(Exception):
    pass


class Game:
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    difficulty = "Easy"
    menace = "Player 2"
    current_player = 'Player 1'
    active = 'active'
    play_speed = 500
    wins = 0
    stalemates = 0
    loss = 0
    win_type = 9

    @staticmethod
    def reset():
        Game.board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        Game.active = 'active'
        Game.current_player = 'Player 1'
        Game.win_type = 9

    @staticmethod
    def check_board():
        board = Game.board
        if (board[0] == board[1] == board[2] and board[0] == 'X'):
            Game.win_type = 0
            return 'Win'
        elif (board[3] == board[4] == board[5] and board[3] == 'X'):
            Game.win_type = 1
            return 'Win'
        elif (board[6] == board[7] == board[8] and board[6] == 'X'):
            Game.win_type = 2
            return 'Win'
        elif (board[0] == board[3] == board[6] and board[0] == 'X'):
            Game.win_type = 3
            return 'Win'
        elif (board[1] == board[4] == board[7] and board[1] == 'X'):
            Game.win_type = 4
            return 'Win'
        elif (board[2] == board[5] == board[8] and board[2] == 'X'):
            Game.win_type = 5
            return 'Win'
        elif (board[0] == board[4] == board[8] and board[0] == 'X'):
            Game.win_type = 6
            return 'Win'
        elif (board[6] == board[4] == board[2] and board[6] == 'X'):
            Game.win_type = 7
            return 'Win'
        elif (board[0] == board[1] == board[2] and board[0] == 'O'):
            Game.win_type = 0
            return 'Loss'
        elif (board[3] == board[4] == board[5] and board[3] == 'O'):
            Game.win_type = 1
            return 'Loss'
        elif (board[6] == board[7] == board[8] and board[6] == 'O'):
            Game.win_type = 2
            return 'Loss'
        elif (board[0] == board[3] == board[6] and board[0] == 'O'):
            Game.win_type = 3
            return 'Loss'
        elif (board[1] == board[4] == board[7] and board[1] == 'O'):
            Game.win_type = 4
            return 'Loss'
        elif(board[2] == board[5] == board[8] and board[2] == 'O'):
            Game.win_type = 5
            return 'Loss'
        elif (board[0] == board[4] == board[8] and board[0] == 'O'):
            Game.win_type = 6
            return 'Loss'
        elif (board[6] == board[4] == board[2] and board[6] == 'O'):
            Game.win_type = 7
            return 'Loss'
        elif '_' not in Game.board:
            return 'Stalemate'
        else:
            return 'Continue'

    @staticmethod
    def board_index():
        Game.board_spaces = []
        for i in range(9):
            if Game.board[i] == '_':
                Game.board_spaces.append(i)


class SelectDiff:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menace")

        def set_diff(diff):
            Game.difficulty = diff
            if diff == "Easy":
                Game.play_speed = 500
            elif diff == "Medium":
                Game.play_speed = 334
            elif diff == "Hard":
                Game.play_speed = 168
            elif diff == "Impossible":
                Game.play_speed = 0
            self.root.destroy()
        # Settings
        self.button_color = 'light gray'

        # Frame Setup
        self.title_frame = tk.Frame(self.root)
        self.button_frame = tk.Frame(self.root)

        self.title_frame.pack()
        self.button_frame.pack()

        # Label Setup
        self.title_label = tk.Label(self.title_frame, text='Please Select a Difficulty')
        self.title_label.pack(pady=10, padx=10)

        # Button Setup
        self.button_easy = tk.Button(self.button_frame, text="Easy", bg=self.button_color, command=lambda: set_diff("Easy"))
        self.button_medium = tk.Button(self.button_frame, text="Medium", bg=self.button_color, command=lambda: set_diff("Medium"))
        self.button_hard = tk.Button(self.button_frame, text="Hard", bg=self.button_color, command=lambda: set_diff("Hard"))
        self.button_impossible = tk.Button(self.button_frame, text="Impossible", bg=self.button_color, command=lambda: set_diff("Impossible"))

        self.button_easy.grid(row=0, column=0, pady=10, padx=10)
        self.button_medium.grid(row=0, column=1, pady=10, padx=10)
        self.button_hard.grid(row=0, column=2, pady=10, padx=10)
        self.button_impossible.grid(row=0, column=3, pady=10, padx=10)

        self.root.mainloop()


class SelectPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menace")

        def set_player(player):
            Game.menace = player
            self.root.destroy()
        # Settings
        self.button_color = 'light gray'

        # Frame Setup
        self.title_frame = tk.Frame(self.root)
        self.button_frame = tk.Frame(self.root)

        self.title_frame.pack()
        self.button_frame.pack()

        # Label Setup
        self.title_label = tk.Label(self.title_frame, text='Please Select to go First or Second?')
        self.title_label.pack(pady=10, padx=10)

        # Button Setup
        self.button_first = tk.Button(self.button_frame, text="I'll go First", bg=self.button_color, command=lambda: set_player("Player 2"))
        self.button_second = tk.Button(self.button_frame, text="I'll go Second", bg=self.button_color, command=lambda: set_player("Player 1"))

        self.button_first.grid(row=0, column=0, pady=10, padx=10)
        self.button_second.grid(row=0, column=1, pady=10, padx=10)

        self.root.mainloop()


class GameWindow:
    def __init__(self):
        print('def __init__()')
        self.root = tk.Tk()
        self.root.title("Menace")

        self.moves = []

        # Frame Setup
        self.menace_title_frame = tk.Frame(self.root)
        self.main_board_frame = tk.Frame(self.root)
        self.player_title_frame = tk.Frame(self.root)

        self.menace_title_frame.grid(row=0, column=0)
        self.main_board_frame.grid(row=1, column=0)
        self.player_title_frame.grid(row=2, column=0)

        # Menace Title Setup
        self.menace_title_label = tk.Label(self.menace_title_frame,
                                           text='M E N A C E', font=('Century Gothic', 20, 'bold'))
        self.menace_subtitle_label = tk.Label(self.menace_title_frame,
                                              text=f'Difficulty: {Game.difficulty}', font=('Century Gothic', 10))

        self.menace_title_label.grid(row=0, column=0)
        self.menace_subtitle_label.grid(row=1, column=0)

        # Main Board Setup
        self.board_h = 600
        self.board_w = 600

        # Player Title Setup

        self.player_title = tk.Label(self.player_title_frame,
                                     text='Menace is Playing...\n', font=('Century Gothic', 10, 'bold'))
        self.player_stats = tk.Label(self.player_title_frame,
                                     text=f'Wins: {Game.wins}   Stalemates: {Game.stalemates}   Losses: {Game.loss}')
        self.player_title.grid(row=0, column=0)
        self.player_stats.grid(row=1, column=0)

        self.drawboard()
        self.take_turn_AI()
        self.root.wait_visibility()
        self.root.mainloop()

    def drawboard(self):
        print('def drawboard()')
        self.main_board = tk.Canvas(self.main_board_frame, bg="white", height=self.board_h, width=self.board_w)
        self.main_board.bind("<Button-1>", self.take_turn_press)
        self.boardlines = [self.main_board.create_line(self.board_w / 3, 0, self.board_w / 3, self.board_h),
                           self.main_board.create_line(2 * self.board_w / 3, 0, 2 * self.board_w / 3, self.board_h),
                           self.main_board.create_line(0, self.board_h / 3, self.board_w, self.board_h / 3),
                           self.main_board.create_line(0, 2 * self.board_h / 3, self.board_w, 2 * self.board_h / 3)]

        self.main_board.pack()

    def checkmove(self, index, x, y):
        print('def checkmove()')
        if Game.active != 'active':
            Game.reset()
            self.main_board.destroy()
            self.drawboard()
            Game.current_player = 'Player 2'
        elif Game.board[index] != '_':
            raise BadMove
        elif Game.current_player == 'Player 1' and Game.menace != 'Player 1' and Game.active == 'active':
            self.X_turn(index, x, y)
        elif Game.current_player == 'Player 2' and Game.menace != 'Player 2' and Game.active == 'active':
            self.Y_turn(index, x, y)
        elif Game.current_player == 'Player 1' and Game.menace == 'Player 1' and Game.active == 'active':
            self.X_turn(index, x, y)
        elif Game.current_player == 'Player 2' and Game.menace == 'Player 2' and  Game.active == 'active':
            self.Y_turn(index, x, y)
        else:
            raise SystemError

    def X_turn(self, index, x, y):
        print('def X_turn()')
        if Game.board[index] != '_':
            pass
        else:
            Game.board[index] = 'X'
            self.place_x(x, y)

    def Y_turn(self, index, x, y):
        print('def Y_turn()')
        if Game.board[index] != '_':
            pass
        else:
            Game.board[index] = 'O'
            self.place_o(x, y)

    def take_turn_press(self, event):
        print('def take_turn_press()')
        x1 = self.board_w / 3
        x2 = 2 * self.board_w / 3
        y1 = self.board_h / 3
        y2 = 2 * self.board_h / 3
        choice = 0
        x = 0
        y = 0
        if event.x <= x1 and event.y <= y1:
            choice = 0
            x = (0 + x1) / 2
            y = (0 + y1) / 2
        elif x1 < event.x <= x2 and event.y <= y1:
            choice = 1
            x = (x1 + x2) / 2
            y = (0 + y1) / 2
        elif event.x > x2 and event.y <= y1:
            choice = 2
            x = (x2 + self.board_w) / 2
            y = (0 + y1) / 2
        elif event.x <= x1 and y1 < event.y <= y2:
            choice = 3
            x = (0 + x1) / 2
            y = (y1 + y2) / 2
        elif x1 < event.x <= x2 and y1 < event.y <= y2:
            choice = 4
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
        elif event.x > x2 and y1 < event.y <= y2:
            choice = 5
            x = (x2 + self.board_w) / 2
            y = (y1 + y2) / 2
        elif event.x <= x1 and event.y > y2:
            choice = 6
            x = (0 + x1) / 2
            y = (y2 + self.board_h) / 2
        elif x1 < event.x <= x2 and event.y > y2:
            choice = 7
            x = (x1 + x2) / 2
            y = (y2 + self.board_h) / 2
        elif event.x > x2 and event.y > y2:
            choice = 8
            x = (x2 + self.board_w) / 2
            y = (y2 + self.board_h) / 2
        try:
            self.checkmove(choice, x, y)
            outcome = Game.check_board()

            if outcome == "Win":
                self.end_game("Menace")
            elif outcome == "Stalemate":
                self.end_game("Stalemate")
            elif outcome == "Loss":
                self.end_game("Win")
            else:
                self.swap()
                self.player_title.config(text='Menace is Playing...\n')
                self.root.after(Game.play_speed, self.take_turn_AI)
        except BadMove:
            pass

    def take_turn_AI(self):
        print('def take_turn_AI()')
        choice = Menace.read_board(Game.board, Game.difficulty, Game.menace)
        x1 = self.board_w / 3
        x2 = 2 * self.board_w / 3
        y1 = self.board_h / 3
        y2 = 2 * self.board_h / 3
        x = 0
        y = 0
        if choice == 0:
            x = (0 + x1) / 2
            y = (0 + y1) / 2
        elif choice == 1:
            x = (x1 + x2) / 2
            y = (0 + y1) / 2
        elif choice == 2:
            x = (x2 + self.board_w) / 2
            y = (0 + y1) / 2
        elif choice == 3:
            x = (0 + x1) / 2
            y = (y1 + y2) / 2
        elif choice == 4:
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
        elif choice == 5:
            x = (x2 + self.board_w) / 2
            y = (y1 + y2) / 2
        elif choice == 6:
            x = (0 + x1) / 2
            y = (y2 + self.board_h) / 2
        elif choice == 7:
            x = (x1 + x2) / 2
            y = (y2 + self.board_h) / 2
        elif choice == 8:
            x = (x2 + self.board_w) / 2
            y = (y2 + self.board_h) / 2
        try:
            self.checkmove(choice, x, y)
            outcome = Game.check_board()

            if outcome == "Win":
                self.end_game("Menace")
            elif outcome == "Stalemate":
                self.end_game("Stalemate")
            elif outcome == "Loss":
                self.end_game("Win")
            else:
                self.swap()
                self.player_title.config(text='Your Turn...\n')
        except BadMove:
            pass

    def place_o(self, x, y):
        print('def place_o()')
        def _create_circle(self, x, y, r, **kwargs):
            return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

        tk.Canvas.create_circle = _create_circle
        self.main_board.create_circle(x, y, 0.8 * self.board_w / 6)

    def place_x(self, x, y):
        print('def place_x()')
        r = 0.8 * self.board_w / 6
        self.main_board.create_line(x - r, y - r, x + r, y + r)
        self.main_board.create_line(x + r, y - r, x - r, y + r)

    def swap(self):
        print('def swap()')
        if Game.current_player == 'Player 1':
            Game.current_player = 'Player 2'
        elif Game.current_player == 'Player 2':
            Game.current_player = 'Player 1'

    def end_game(self, result):
        print('def end_game()')
        Game.active = 'inactive'
        if result == "Menace":
            Game.loss += 1
            self.player_title.config(text='Menace Wins\nClick the board to play again')
            self.player_stats.config(text=f'Wins: {Game.wins}   Stalemates: {Game.stalemates}   Losses: {Game.loss}')
        elif result == "Stalemate":
            Game.stalemates += 1
            self.player_title.config(text='Stalemate\nClick the board to play again')
            self.player_stats.config(text=f'Wins: {Game.wins}   Stalemates: {Game.stalemates}   Losses: {Game.loss}')
        elif result == "Win":
            Game.wins += 1
            self.player_title.config(text='You Win!\nClick the board to play again')
            self.player_stats.config(text=f'Wins: {Game.wins}   Stalemates: {Game.stalemates}   Losses: {Game.loss}')

        linewidth = 5
        color = 'red'

        if Game.win_type == 0:
            r = 0.9 * self.board_w / 2
            x = self.board_w/2
            y = self.board_h/6
            self.main_board.create_line(x - r, y, x + r, y, width=linewidth, fill=color)
        elif Game.win_type == 1:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 2
            y = self.board_h / 2
            self.main_board.create_line(x - r, y, x + r, y, width=linewidth, fill=color)
        elif Game.win_type == 2:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 2
            y = 5 * self.board_h / 6
            self.main_board.create_line(x - r, y, x + r, y, width=linewidth, fill=color)
        elif Game.win_type == 3:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 6
            y = self.board_h / 2
            self.main_board.create_line(x, y - r, x, y + r, width=linewidth, fill=color)
        elif Game.win_type == 4:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 2
            y = self.board_h / 2
            self.main_board.create_line(x, y - r, x, y + r, width=linewidth, fill=color)
        elif Game.win_type == 5:
            r = 0.9 * self.board_w / 2
            x = 5 * self.board_w / 6
            y = self.board_h / 2
            self.main_board.create_line(x, y - r, x, y + r, width=linewidth, fill=color)
        elif Game.win_type == 6:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 2
            y = self.board_h / 2
            self.main_board.create_line(x - r, y - r, x + r, y + r, width=linewidth, fill=color)
        elif Game.win_type == 7:
            r = 0.9 * self.board_w / 2
            x = self.board_w / 2
            y = self.board_h / 2
            self.main_board.create_line(x - r, y + r, x + r, y - r, width=linewidth, fill=color)
        else:
            pass


diff_select = SelectDiff()
player_select = SelectPlayer()
main_window = GameWindow()
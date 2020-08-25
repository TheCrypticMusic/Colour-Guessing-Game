import tkinter as tk
import random


class Application(tk.Frame):
    """GUI for the colour guessing game"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()
        self.colour_text['text'] = self.colour_list()
        self.colour_text['fg'] = self.colour_list()

        self.incorrect_score = 0
        self.incorrect['text'] = f'Incorrect: {self.incorrect_score}'

        self.correct_score = 0
        self.correct['text'] = f'Correct: {self.correct_score}'
        self.seconds = 60
        self.timer['text'] = f'Timer: {self.seconds}'
        self.timer.after(1000, self.countdown)


    def correct_answer(self):
        self.correct_score += 1
        self.correct['text'] = f'Correct: {self.correct_score}'
        self.colour_text['text'] = self.colour_list()
        self.colour_text['fg'] = self.colour_list()

    def incorrect_answer(self):
        self.incorrect_score += 1
        self.incorrect['text'] = f'Incorrect: {self.incorrect_score}'
        self.colour_text['text'] = self.colour_list()
        self.colour_text['fg'] = self.colour_list()

    def countdown(self):
        """Logic for the timer to countdown in 1 second intervals"""
        self.seconds -= 1
        self.timer['text'] = f'Timer: {self.seconds}'
        self.timer.after(1000, self.countdown)
        if self.seconds == 0:
            self.timer['text'] = f'Times up'
            self.timer['fg'] = 'red'
            self.seconds += 1

    def entry_field(self, event=None):
        """Controls the Entry box. Checks the user's answer with the random text/ colour assigned to it"""
        answer = self.entry.get()
        self.entry.delete(0, 'end')
        if answer.lower() == self.colour_text['fg'].lower():
            self.correct_answer()
        else:
            self.incorrect_answer()

    def colour_list(self):
        """Iterates a random colour to be displayed for user
        Returns:
            List: Colour
        """
        self.colours = ['Blue', 'Orange', 'Red', 'Green']
        self.rand_colours = random.choice(self.colours)
        return self.rand_colours

    def reset_game(self):
        """Restores the values to the original state"""
        self.correct_score = 0
        self.incorrect_score = 0
        self.seconds = 60
        self.correct['text'] = f'Correct: {self.correct_score}'
        self.incorrect['text'] = f'Incorrect: {self.incorrect_score}'

    def create_widgets(self):
        """Display widgets that make up the application"""
        self.title = tk.Label(self, text='COLOUR GAME', font='Helvetica 22 bold')
        self.title.pack()

        self.rules = tk.Label(self, text='Type the colour of the text.')
        self.rules.pack()

        self.timer = tk.Label(self, text=None, fg='green')
        self.timer.pack(pady=5)

        self.colour_text = tk.Label(self, font='Helvetica 18 bold')
        self.colour_text.pack()

        self.entry = tk.Entry(self)
        self.entry.bind('<Return>', self.entry_field)
        self.entry.pack(pady=5)

        self.correct = tk.Label(self, fg='green')
        self.correct.pack(pady=10)

        self.incorrect = tk.Label(self, fg='red')
        self.incorrect.pack()

        self.button_frame = tk.Frame(self, padx=10)
        self.button_frame.pack(fill=tk.BOTH)

        self.reset_button = tk.Button(self.button_frame, text='RESET', command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT, pady=20, padx=20)

        self.quit = tk.Button(self.button_frame, text="QUIT", command=self.master.destroy)
        self.quit.pack(side=tk.RIGHT, pady=20, padx=20)


root = tk.Tk()
root.geometry('300x300')
root.title('Colour Guessing Game')
app = Application(master=root)
app.mainloop()

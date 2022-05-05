# Runs GUI with no working buttons as of v1.

from tkinter import *
from functools import partial
import re


class Home:
    def __init__(self):
        background_colour = "orange"

        # Home screen Frame
        self.home_frame = Frame(bg=background_colour, pady=10, padx=20)
        self.home_frame.grid(row=0)

        # Maori Quiz Title Label
        self.quiz_heading_label = Label(self.home_frame,
                                        text="Maori Quiz",
                                        font="Arial 32 bold",
                                        bg="yellow", pady=10,
                                        padx=20)
        self.quiz_heading_label.grid(row=1)

        # Description Label
        self.user_instructions = Label(self.home_frame,
                                       text="Press 'Start' to begin the quiz...",
                                       font="Arial 10 italic", wrap=290,
                                       justify=LEFT, bg=background_colour,
                                       padx=10, pady=10)
        self.user_instructions.grid(row=2)

        # Start Quiz Button
        self.start_quiz_button = Button(self.home_frame, text="START QUIZ",
                                        font="Arial 25 bold", bg="green",
                                        pady=10, padx=10)
        self.start_quiz_button.grid(row=3)

        # Frame that contains Stats and Help buttons
        self.bottom_frame = Frame(bg=background_colour, pady=10, padx=20)
        self.bottom_frame.grid(row=1)

        # Stats Button
        self.stats_button = Button(self.bottom_frame, text=" STATS ",
                                   font="Arial 18 bold", bg="blue",
                                   pady=10, padx=13)
        self.stats_button.grid(row=0, column=0)

        # Help Button
        self.help_button = Button(self.bottom_frame, text=" HELP ",
                                  font="Arial 18 bold", bg="red",
                                  pady=10, padx=13)
        self.help_button.grid(row=0, column=1)

if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Home()
    root.mainloop()

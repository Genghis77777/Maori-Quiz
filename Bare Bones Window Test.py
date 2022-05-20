# Based off of Questions v1

from tkinter import *
from functools import partial  # To prevent unwanted windows


class Home:
    def __init__(self):
        background_colour = "orange"

        # Home screen Frame
        self.home_frame = Frame(bg=background_colour, pady=10, padx=20)
        self.home_frame.grid(row=0)

        # Start Quiz Button
        self.start_quiz_button = Button(self.home_frame, text="START QUIZ",
                                        font="Arial 25 bold", bg="green",
                                        pady=10, padx=10, command=self.questions)
        self.start_quiz_button.grid(row=3)

    def questions(self):
        get_questions = End_screen(self)


class End_screen:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        # partner.answer_two_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.end_screen_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.end_screen_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.end_screen_frame = Frame(self.end_screen_box, width=300, bg=background)
        self.end_screen_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.end_screen_frame,
                                             text="End Screen",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.end_screen_frame,
                                   text="You got x answers right!",
                                   font="Arial 12 italic", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Return to home frame
        self.return_to_start_frame = Frame(self.end_screen_box, width=300, bg=background)
        self.return_to_start_frame.grid(row=1)

        # Return to home Button
        self.return_to_home_button = Button(self.return_to_start_frame, text="Return to Start",
                                            font="Arial 21 bold", bg="green", pady=10,
                                            padx=10, width=27,
                                            command=self.home_screen)
        self.return_to_home_button.grid(row=0, column=1)

        # Close button (row 2)
        self.close_button = Button(self.return_to_start_frame, text="Close", width=10,
                                   bg="red", font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.end_screen_box.destroy()

    def home_screen(self):
        get_home_screen = Home()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Home()
    root.mainloop()

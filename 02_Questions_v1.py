from tkinter import *
from functools import partial  # To prevent unwanted windows


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
                                        pady=10, padx=10, command=self.questions)
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

    def questions(self):
        get_questions = Questions(self)
        get_questions.questions_text.configure(text="Questions text goes here")


class Questions:
    def __init__(self, partner):
        background = "orange"

        # Disable Questions button
        partner.start_quiz_button.config(state=DISABLED)

        # Sets up child window (ie: questions box)
        self.questions_box = Toplevel()

        # If users press cross at top, closes questions and 'releases' questions button
        self.questions_box.protocol('WM_DELETE_WINDOW', partial(self.close_questions, partner))

        # Set up GUI Frame
        self.questions_frame = Frame(self.questions_box, width=300, bg=background)
        self.questions_frame.grid()

        # Set up Question number heading (row 0)
        self.how_heading = Label(self.questions_frame, text="Question 1",
                                 font=("Arial", "10", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Question text (label, row 1)
        self.questions_text = Label(self.questions_frame, text="", justify=LEFT,
                                    width=40, bg=background, wrap=250)
        self.questions_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.questions_frame, text="Dismiss", width=10, bg="orange",
                                  font="arial 10 bold",
                                  command=partial(self.close_questions, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_questions(self, partner):
        # Put start button back to normal...
        partner.start_quiz_button.config(state=NORMAL)
        self.questions_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Home()
    root.mainloop()

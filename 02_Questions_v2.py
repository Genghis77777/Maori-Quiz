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
                                        pady=10, padx=10, command=self.question)
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

    def question(self):
        get_question = Question(self)


class Question:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.start_quiz_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_one_box = Toplevel()

        # Set up GUI Frame
        self.question_frame = Frame(self.question_one_box, width=200, bg=background)
        self.question_frame.grid(row=0)

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question One",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for [English word] in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background, wrap=250)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_one_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Answer 1",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Answer 2",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Answer 3",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Answer 4",
                                         font="Arial 12", bg="red", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Home()
    root.mainloop()

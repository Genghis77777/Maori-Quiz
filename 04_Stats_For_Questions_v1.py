# Right answers are collected and displayed in the end screen,
# Wrong answers don't yet open the next question

from tkinter import *
from functools import partial  # To prevent unwanted windows

right_answers = 0


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
                                       font="Arial 10 italic",
                                       justify=LEFT, bg=background_colour,
                                       padx=10, pady=10)
        self.user_instructions.grid(row=2)

        # Start Quiz Button
        self.start_quiz_button = Button(self.home_frame, text="START QUIZ",
                                        font="Arial 25 bold", bg="green",
                                        pady=10, padx=10, command=self.question_1)
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

    def question_1(self):
        get_question = Question_1(self)


class Question_1:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.start_quiz_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_one_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_one_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_one_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question One",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Apple' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_one_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Panana",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Karepe",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Aporo",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width,
                                          command=self.question_2_correct)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Ripanga",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.start_quiz_button.config(state=NORMAL)
        self.question_one_box.destroy()

    def question_2_correct(self):
        get_correct = Question_2(self)
        global right_answers
        right_answers += 1
        self.question_one_box.destroy()

    def question_2_incorrect(self):
        get_correct = Question_2(self)
        self.question_one_box.destroy()


class Question_2:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_three_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_two_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_two_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_two_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Two",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Table' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_two_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Waka",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Ripanga",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width,
                                        command=self.question_3_correct)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Kakariki",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Rakau",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_two_box.destroy()

    def question_3_correct(self):
        get_correct = Question_3(self)
        global right_answers
        right_answers += 1
        self.question_two_box.destroy()

    def question_3_incorrect(self):
        get_correct = Question_3(self)
        self.question_two_box.destroy()


class Question_3:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_two_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_three_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_three_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_three_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Three",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Dog' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_three_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Kuri",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width,
                                        command=self.question_4_correct)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Rapeti",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Peia",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Kahurangi",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_three_box.destroy()

    def question_4_correct(self):
        get_correct = Question_4(self)
        global right_answers
        right_answers += 1
        self.question_three_box.destroy()

    def question_4_incorrect(self):
        get_correct = Question_4(self)
        self.question_three_box.destroy()


class Question_4:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_one_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_four_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_four_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_four_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Four",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Sponge' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_four_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Pereki",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Paru",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Totohu",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Hautai",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width,
                                         command=self.question_5_correct)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_four_box.destroy()

    def question_5_correct(self):
        get_correct = Question_5(self)
        global right_answers
        right_answers += 1
        self.question_four_box.destroy()

    def question_5_incorrect(self):
        get_correct = Question_5(self)
        self.question_four_box.destroy()


class Question_5:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_four_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_five_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_five_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_five_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Five",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Hand' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_five_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Upoko",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Ringa",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Waewae",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width,
                                          command=self.question_6_correct)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Ihu",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_five_box.destroy()

    def question_6_correct(self):
        get_correct = Question_6(self)
        global right_answers
        right_answers += 1
        self.question_five_box.destroy()

    def question_6_incorrect(self):
        get_correct = Question_6(self)
        self.question_five_box.destroy()


class Question_6:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_three_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_six_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_six_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_six_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Six",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Goose' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_six_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Te Pihoihoi",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Kuihi",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width,
                                        command=self.question_7_correct)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Waaka",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Parera",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_six_box.destroy()

    def question_7_correct(self):
        get_correct = Question_7(self)
        global right_answers
        right_answers += 1
        self.question_six_box.destroy()

    def question_7_incorrect(self):
        get_correct = Question_7(self)
        self.question_six_box.destroy()


class Question_7:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_three_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_seven_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_seven_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_seven_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Seven",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Pink' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_seven_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Mawhero",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width,
                                        command=self.question_8_correct)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Hua Manu",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Waiporoporo",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Phero",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_seven_box.destroy()

    def question_8_correct(self):
        get_correct = Question_8(self)
        global right_answers
        right_answers += 1
        self.question_seven_box.destroy()

    def question_8_incorrect(self):
        get_correct = Question_8(self)
        self.question_seven_box.destroy()


class Question_8:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_one_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_eight_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_eight_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_eight_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Eight",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Phone' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_eight_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Rorohiko",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Pouaka Whakaata",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Papa",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Waea",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width,
                                         command=self.question_9_correct)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10, bg="red",
                                   font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_eight_box.destroy()

    def question_9_correct(self):
        get_correct = Question_9(self)
        global right_answers
        right_answers += 1
        self.question_eight_box.destroy()

    def question_9_incorrect(self):
        get_correct = Question_9(self)
        self.question_eight_box.destroy()

class Question_9:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_four_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_nine_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_nine_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_nine_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Nine",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Grass' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_nine_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Ngaherehere",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Tarutaru",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Mahuri",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width,
                                          command=self.question_10_correct)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Rakau",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10,
                                   bg="red", font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_nine_box.destroy()

    def question_10_correct(self):
        get_correct = Question_10(self)
        global right_answers
        right_answers += 1
        self.question_nine_box.destroy()

    def question_10_incorrect(self):
        get_correct = Question_10(self)
        self.question_nine_box.destroy()


class Question_10:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_three_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_ten_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.question_ten_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.question_frame = Frame(self.question_ten_box, width=300, bg=background)
        self.question_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.question_frame,
                                             text="Question Ten",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame,
                                   text="What is the word for 'Heart' in Maori?",
                                   font="Arial 14 italic bold", width=40,
                                   bg=background)
        self.question_text.grid(row=1)

        # Answer boxes frame
        self.answer_frame = Frame(self.question_ten_box, width=300, bg=background)
        self.answer_frame.grid(row=1)

        answer_button_width = 24

        # Answer 1 Button
        self.answer_one_button = Button(self.answer_frame, text="Te Puku",
                                        font="Arial 12", bg="green", pady=10,
                                        padx=10, width=answer_button_width)
        self.answer_one_button.grid(row=0, column=0)

        # Answer 2 Button
        self.answer_two_button = Button(self.answer_frame, text="Ngakau",
                                        font="Arial 12", bg="purple", pady=10,
                                        padx=10, width=answer_button_width,
                                        command=self.end_screen_correct)
        self.answer_two_button.grid(row=0, column=1)

        # Answer 3 Button
        self.answer_three_button = Button(self.answer_frame, text="Takihi",
                                          font="Arial 12", bg="blue", pady=10,
                                          padx=10, width=answer_button_width)
        self.answer_three_button.grid(row=1, column=0)

        # Answer 4 Button
        self.answer_four_button = Button(self.answer_frame, text="Taringa",
                                         font="Arial 12", bg="brown", pady=10,
                                         padx=10, width=answer_button_width)
        self.answer_four_button.grid(row=1, column=1)

        # Close button (row 2)
        self.close_button = Button(self.answer_frame, text="Close", width=10,
                                   bg="red", font="arial 10 bold",
                                   command=partial(self.close_question, partner))
        self.close_button.grid(row=2, column=1, pady=10)

    def close_question(self, partner):
        # Put start button back to normal...
        partner.answer_three_button.config(state=NORMAL)
        self.question_ten_box.destroy()

    def end_screen_correct(self):
        global right_answers
        right_answers += 1
        get_correct = End_screen(self)
        self.question_ten_box.destroy()

    def end_screen_incorrect(self):
        get_correct = End_screen(self)
        self.question_ten_box.destroy()


class End_screen:
    def __init__(self, partner):
        background = "orange"

        # Disable Start Quiz button
        partner.answer_two_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.end_screen_box = Toplevel()

        # If users press cross at top, closes question and 'releases' question button
        self.end_screen_box.protocol('WM_DELETE_WINDOW', partial(self.close_question, partner))

        # Set up GUI Frame
        self.end_screen_frame = Frame(self.end_screen_box, width=300, height=300, bg=background)
        self.end_screen_frame.grid()

        # Set up Question number heading (row 0)
        self.question_number_heading = Label(self.end_screen_frame,
                                             text="End Screen",
                                             font="Arial 32 bold",
                                             bg="yellow", pady=10,
                                             padx=20, width=17)
        self.question_number_heading.grid(row=0)

        global right_answers

        # Question text (label, row 1)
        self.question_text = Label(self.end_screen_frame,
                                   text="You got {} answers right!".format(right_answers),
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
        self.end_screen_box.destroy()

    def home_screen(self):
        get_home_screen = Home()
        self.end_screen_box.destroy()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Home()
    root.mainloop()

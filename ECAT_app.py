import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("First project")

frame = LabelFrame(
    root,
    text="ECAT app...",
    padx=50,
    pady=50,
    background="#007875",
    width=1300,
    height=760
)
frame.pack(padx=5, pady=5)
frame.pack_propagate(False)

questions = [
    "Which one is not a branch of physical sciences?",
    "Which branch of science plays an important role in the development of technology and engineering?",
    "The number of categories in which physical quantities are divided are?",
    "How many types of units are in SI?",
    "In scientific notation numbers are expressed in",
    "Random errors can be reduced by taking?",
    "The uncertainty in a measurement may occur due to",
    "Preftix deca represents",
    "The error in measurement may occur due to?",
    "1024 can be written in scientific notation as?",
]

answers_choice = [
    ["A. chemistry", "B. astronomy", "C. geology", "D. biology"],
    ["A. chemistry", "B. physics", "C. geology", "D. biology"],
    ["one", "two", "three", "four"],
    ["one", "two", "three", "four"],
    ["power of 10", "power of 2", "reciprocal", "decimal"],
    ["average", "difference", "sum", "product"],
    ["limitation of an instrument", "natural variation of the object to be measured", "inadequate of technique",
     "all given in a , b and c"],
    ["10 Raised to power 1", "10 Raised to power 2", "10 Raised to power 3", "10 Raised to power -1"],
    ["inexperience of a person", "the faulty apparantus", "inappropriate method", "due to all reasons in a, b and c"],
    ["1.024x103", "2 Raised to power 10", "0.000976", "1/0.00097"],
]

answers = [3, 1, 1, 2, 0, 0, 3, 0, 3, 0]

user_answer = []

ques = 0


def show_result(score, correct_answers, wrong_answers, skipped_questions):
    # Destroy existing widgets
    lbl_Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    btn_skip.destroy()
    btn_submit.destroy()

    # Display the score on the same frame
    score_label = Label(
        frame,
        text=f"Your score is: {score}\n\n"
             f"Correct Answers: {correct_answers}\n"
             f"Wrong Answers: {wrong_answers}\n"
             f"Skipped Questions: {skipped_questions}",
        font=("Comic Sans MS", 16),
        background="#007875"
    )
    score_label.pack(pady=20)


def calc():
    global ques, user_answer
    x = 0
    score = 0
    correct_answers = 0
    wrong_answers = 0
    skipped_questions = 0

    while len(user_answer) < len(questions):
        user_answer.append(-1)

    for i in range(len(questions)):
        if user_answer[i] == -1:
            skipped_questions += 1
        elif user_answer[i] == answers[i]:
            score += 10
            correct_answers += 1
        else:
            wrong_answers += 1
    show_result(score, correct_answers, wrong_answers, skipped_questions)
    destroy_widgets()


def destroy_widgets():
    lbl_instruction.destroy()
    lbl_rules.destroy()
    btn_start.destroy()

    label_image.destroy()
    label_text.destroy()

    btn_submit.destroy()
    btn_skip.destroy()

    lbl_Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()


def create_skip_submit_buttons():
    global btn_skip, btn_submit
    btn_skip = Button(
        frame,
        text="Skip",
        command=selected,
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_skip.pack(side=BOTTOM, padx=20, pady=20)

    btn_submit = Button(
        frame,
        text="Submit",
        command=calc,
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_submit.pack(side=BOTTOM, padx=20, pady=20)


def selected():
    global radio_var, lbl_Questions, r1, r2, r3, r4, user_answer, ques
    x = radio_var.get()
    user_answer.append(x)
    radio_var.set(-1)
    if ques < len(questions) - 1:
        ques += 1
        lbl_Questions.config(text=questions[ques])
        r1['text'] = answers_choice[ques][0]
        r2['text'] = answers_choice[ques][1]
        r3['text'] = answers_choice[ques][2]
        r4['text'] = answers_choice[ques][3]
    else:
        btn_skip.config(state=DISABLED)  # Disable skip button when all questions are answered
        calc()  # Call calc() function to calculate the score


def start_quiz():
    global lbl_Questions, ques
    lbl_Questions = Label(
        frame,
        text=questions[ques],
        font=("Comic Sans MS", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#007875"

    )
    lbl_Questions.pack(pady=(100, 30))

    global radio_var, r1, r2, r3, r4
    radio_var = IntVar()
    radio_var.set(-1)

    r1 = Radiobutton(
        frame,
        text=answers_choice[ques][0],
        font=("Comic Sans MS", 12),
        value=0,
        variable=radio_var,
        command=selected,
        background="#007875"
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        frame,
        text=answers_choice[ques][1],
        font=("Comic Sans MS", 12),
        value=1,
        variable=radio_var,
        command=selected,
        background="#007875"
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        frame,
        text=answers_choice[ques][2],
        font=("Comic Sans MS", 12),
        value=2,
        variable=radio_var,
        command=selected,
        background="#007875"
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        frame,
        text=answers_choice[ques][3],
        font=("Comic Sans MS", 12),
        value=3,
        variable=radio_var,
        command=selected,
        background="#007875"
    )
    r4.pack(pady=5)


def startButtonPressed():
    global label_image, label_text, btn_start, lbl_instruction, lbl_rules, ques
    label_image.destroy()
    label_text.destroy()
    btn_start.destroy()
    lbl_instruction.destroy()
    lbl_rules.destroy()
    create_skip_submit_buttons()  # Call the function to create skip and submit buttons
    start_quiz()


def create_widgets():
    global label_image, label_text, btn_start, lbl_instruction, lbl_rules

    create_header()
    create_instruction_label()
    create_start_button()
    create_rules_label()


def create_header():
    global label_image, label_text
    label_image = Label(
        frame,
        image=img1,
        background="#007875"
    )
    label_image.pack()

    label_text = Label(
        frame,
        text="Welcome to UET ECAT",
        font=("Comic Sans MS", 24, "bold"),
        bg="#007875"
    )
    label_text.pack(pady=(40, 0))


def create_start_button():
    global btn_start
    btn_start = Button(
        frame,
        text="Start",
        command=startButtonPressed,
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_start.pack(pady=(20, 5))


def create_instruction_label():
    global lbl_instruction
    lbl_instruction = Label(
        frame,
        text="Read the rules\nClick start when you are ready",
        bg="#007875",
        font=("Comic Sans MS", 14),
        justify="center"
    )
    lbl_instruction.pack(pady=(10, 0))


def create_rules_label():
    global lbl_rules
    lbl_rules = Label(
        frame,
        text="You will get 20 minutes to solve the quiz",
        width=100,
        font=("Times", 14),
        background="#007875",
        foreground="#FACA2F"
    )
    lbl_rules.pack(pady=(10, 0))


img1 = PhotoImage(file="uet.png")

label_image = None
label_text = None
btn_start = None
lbl_instruction = None
lbl_rules = None

create_widgets()

root.mainloop()

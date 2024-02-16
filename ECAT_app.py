import tkinter
from tkinter import *

root=tkinter.Tk()
root.title("ECAT")
root.geometry("700x600")
root.configure(background="#ffffff")

img1=PhotoImage(file="uet.png")
img2=PhotoImage(file="START-QUIZ-1.png")

label_image = None
label_text = None
btn_start = None
lbl_instruction = None
lbl_rules = None

def create_widgets():
    global label_image, label_text, btn_start, lbl_instruction, lbl_rules

    create_header()
    create_instruction_label()
    create_rules_label()
    create_start_button()

def create_header():
    global label_image, label_text
    label_image = Label(root, image=img1, background="#ffffff")
    label_image.pack()

    label_text = Label(root, text="Welcome to UET ECAT", font=("Comic Sans MS", 24, "bold"), bg="#ffffff")
    label_text.pack(pady=(40, 0))

def create_start_button():
    global btn_start
    btn_start = Button(root, text="Start", command=startButtonPressed, relief=RAISED, border=2, background="#ffffff", font=("Comic Sans MS", 16))
    btn_start.pack(pady=(20, 0))

def start_quiz():
    # Add your code to start the quiz here
    pass  # Placeholder, replace with actual functionality

def startButtonPressed():
    global label_image, label_text, btn_start, lbl_instruction, lbl_rules
    label_image.destroy()
    label_text.destroy()
    btn_start.destroy()
    lbl_instruction.destroy()
    lbl_rules.destroy()

def create_instruction_label():
    global lbl_instruction
    lbl_instruction = Label(root, text="Read the rules\nClick start when you are ready", bg="#ffffff", font=("Comic Sans MS", 14), justify="center")
    lbl_instruction.pack(pady=(10, 0))

def create_rules_label():
    global lbl_rules
    lbl_rules = Label(root, text="This quiz contains 20 questions\nYou will get 20 minutes to solve the quiz\nOnce you select a radio button that will be a final choice\nThe quiz will start as soon as you click the start button",
               width=100, font=("Times", 14), background="#ffffff", foreground="#FACA2F")
    lbl_rules.pack(pady=(10,0))

create_widgets()
root.mainloop()

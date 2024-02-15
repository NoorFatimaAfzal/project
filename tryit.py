import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("ECAT")
root.geometry("700x600")
root.configure(background="#ffffff")

img1 = PhotoImage(file="uet.png")
img2 = PhotoImage(file="START-QUIZ-1.png")

def create_widgets():
    create_header()
    create_instruction_label()
    create_start_button()


def create_header():
    label_image = Label(root, image=img1, background="#ffffff")
    label_image.pack()

    label_text = Label(root, text="Welcome to UET ECAT", font=("Comic Sans MS", 24, "bold"), bg="#ffffff")
    label_text.pack(pady=(40, 0))

def create_start_button():
    btn_start = Button(root, image=img2, relief=FLAT, border=0)
    btn_start.pack()

def create_instruction_label():
    lbl_instruction = Label(root, text="Read the rules\nClick start when you are ready", bg="#ffffff", font=("Comic Sans MS", 14), justify="center")
    lbl_instruction.pack(pady=(10, 0))

create_widgets()

root.mainloop()
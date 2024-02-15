import tkinter
from tkinter import *



def startIsPressed():
    labelimage.destroy()
    labeltext.destroy()
    lblinstruction.destroy()
    lblrules.destroy()
    btnstart.destroy()

    






root=tkinter.Tk()
root.title("ECAT")
root.geometry("700x600")
root.configure(background="#ffffff")
root.resizable(0,0)


img1=PhotoImage(file="uet.png")

labelimage=Label(root,
                 image=img1,
                 background="#ffffff")
labelimage.pack()

labeltext=Label(
                root,text="Welcome to UET ECAT",
                font=("Comic Sans MS",24,"bold"),
                bg="#ffffff")
labeltext.pack(pady=(40,0))

img2=PhotoImage(file="START-QUIZ-1.png")

btnstart=Button(root,
                image=img2,
                relief=FLAT,
                border=0,
                command=startIsPressed)
btnstart.pack()

lblinstruction=Label(root,
                     text="Read the rules\nClick start when you are ready",
                     bg="#ffffff",
                     font=("Comic Sans MS",14),
                     justify="center")
lblinstruction.pack(pady=(10,100))

lblrules=Label(root,
               text="This quiz contains 20 questions\nYou will get 20 minutes to solve the quiz\nOnce you select a radio button that will be a final choice\nThe quiz will start as soon as you click the start button",
               width=100,font=("Times",14),
               background="#000000",
               foreground="#FACA2F")




root.mainloop()
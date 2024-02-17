from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()   
root.title("Login Page")
root.iconbitmap("favicon.ico")  
root.configure(background="#007875")
root.geometry("1300x760")

global label1, label2, label3, entry1, entry2, button

def login():
    username = entry1.get()
    password = entry2.get()
    if username == "" and password == "":
        messagebox.showerror("Login", "Please enter username and password")
    elif username == "noor" and password == "butt":
        messagebox.showinfo("Login", "Login successful")    
    else:
        messagebox.showerror("Login", "Login failed")

label1 = Label(
    root, 
    text="Login Page", 
    font=("Comic Sans MS", 30), 
    background="#007875", 
    fg="black"
)
label1.place(x=500, y=20)    

label2 = Label(
    root, 
    text="Username: ", 
    font=("Comic Sans MS", 20), 
    background="#007875", 
    fg="black"
)
label2.place(x=400, y=190)

label3 = Label(
    root, 
    text="Password: ", 
    font=("Comic Sans MS", 20), 
    background="#007875", 
    fg="black"
)
label3.place(x=400, y=340)

entry1 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black"
)
entry1.place(x=600, y=200)

entry2 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
    show="."
)
entry2.place(x=600, y=350)

button = Button(
    root, 
    text="Login", 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
    command=login
)
button.place(x=550, y=500)

root.mainloop()

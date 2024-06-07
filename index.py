from tkinter import *
from tkinter import messagebox
from tkinter import ttk

jan = Tk()
jan.title("Teste - Painel de Login")
jan.geometry("600x300")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

logo = PhotoImage(file="logo.png")

LeftFrame = Frame(jan, width=200, height=300, bg="GREY", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="BLACK", relief="raised")
RightFrame.pack(side=RIGHT)

LogoLabel = Label (LeftFrame, image=logo, width=100, height=100, bg="GREY")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Comic Sans", 20), bg="GREY", fg="White")
UserLabel.place(x=5, y=100)

UserEntry= ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Comic Sans", 20), bg="GREY", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=150, y=160)

#Buttons

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

RegisterButton = ttk.Button(RightFrame, text="register", width=20)
RegisterButton.place(x=125, y=260)

jan.mainloop()
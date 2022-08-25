from tkinter import *

root = Tk()
root.title("Login")
root.geometry("925x500+200+200")
root.configure(bg="#fff")
root.resizable(False, False)

#img = PhotoImage(file="signin/login.png")
# Label(root, image=img, bg="white").place(x=50, y=50)
Label(root, bg="blue").place(x=50, y=50)


frame = Frame(root, width=350, height=350, bg="red")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white")

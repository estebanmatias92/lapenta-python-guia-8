from tkinter import *
from tkinter import messagebox
import ast

# THe window for the sign in
signin_window = Tk()
signin_window.title("Login")
signin_window.geometry("925x500+300+200")
signin_window.configure(bg="#fff")
signin_window.resizable(False, False)


# Event of signing in
def signin():
    # Get the data introduced by the user
    username = username_entry.get()
    password = password_entry.get()
    # Avoid repeating the file path everywhere
    database = "db/datasheet.txt"

    # Open the "database file" and store the data in an object
    file = open(database, "r+")
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    # If the user and password are correct, the show a grettings screen
    # Otherwise show an error
    if username in r.keys() and password == r[username]:
        screen = Toplevel(signin_window)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(
            screen,
            text="Hello Everyone!",
            bg="#fff",
            fg="black",
            font=("Arial", 50, "bold"),
        ).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror("Invalid", "invalid username or password")


def open_signup_window():
    ##
    ## Duplicaba todo el codigo, igualmente no me salvo de copiar todo dentro
    ## de esta funcion, pero esto es todo la funcionalidad de registro
    ## que deberia estar separado y menos mierdoso... Peor tutorial que agarre... ever
    ##
    # THe window for the signup
    signup_window = Toplevel()
    signup_window.title("Sign up")
    signup_window.geometry("925x500+300+200")
    signup_window.configure(bg="#fff")
    signup_window.resizable(False, False)

    # Event of signing up
    def signup():
        # Get the data introduced by the user
        username = username_entry.get()
        password = password_entry.get()
        confirmed_password = confirm_password_entry.get()
        # Avoid repeating the file path everywhere
        database = "db/datasheet.txt"

        # If everything is ok, store open the .txt file in write mode and store the data
        # Otherwise throw an error
        if password == confirmed_password:
            try:
                file = open(database, "r+")
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file = open(database, "w")
                file.write(str(r))

                messagebox.showinfo("Signup", "Successfully signed up")
            except:
                file = open(database, "w")
                pp = str({"Username": "password"})
                file.write(pp)

            finally:
                file.close()  # Close the file "database" no matter what

        else:
            messagebox.showerror("Invalid", "Both passwords should match")

    # Event when the sign in button is pressed in the sign up window
    def open_signin_window():
        signup_window.destroy()

    # Images for the window
    # img = PhotoImage(file="signup.png") # Descomentar esta linea si se tiene la imagen
    # signup_window_decoration = Label(root, image=img, bg="white") # Descomentar esta linea si se tiene la imagen
    signup_window_decoration = Label(
        signup_window, bg="blue"
    )  # Borrar esta linea si se tiene la imagen
    signup_window_decoration.place(x=50, y=50)

    # Background of the form
    signup_form_frame = Frame(signup_window, width=350, height=390, bg="#fff")
    signup_form_frame.place(x=480, y=50)

    # Visible title of the form
    signup_form_heading = Label(
        signup_form_frame,
        text="Sign up",
        fg="#57a1f8",
        bg="white",
        font=("Consolas", 23, "bold"),
    )
    signup_form_heading.place(x=100, y=5)

    ##########----------------------------------------------------------------------

    # Remove the Username input placeholder
    def remove_username_placeholder(e):
        username_entry.delete(0, "end")

    # Restore the Username input placeholder
    def restore_username_placeholder(e):
        input_data = username_entry.get()
        if not input_data:
            username_entry.insert(0, "Username")

    # Username text box
    username_entry = Entry(
        signup_form_frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Consolas", 11),
    )
    username_entry.place(x=30, y=80)
    username_entry.insert(0, "Username")
    username_entry.bind("<FocusIn>", remove_username_placeholder)
    username_entry.bind("<FocusOut>", restore_username_placeholder)

    # Draw a line below the Input Text box
    Frame(signup_form_frame, width=295, height=2, bg="black").place(x=25, y=107)
    ##########----------------------------------------------------------------------
    ##########----------------------------------------------------------------------

    # Remove the Password input placeholder
    def remove_password_placeholder(e):
        password_entry.delete(0, "end")

    # Restore the Password input placeholder
    def restore_password_placeholder(e):
        input_data = password_entry.get()
        if not input_data:
            password_entry.insert(0, "Password")

    # Password text box
    password_entry = Entry(
        signup_form_frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Consolas", 11),
    )
    password_entry.place(x=30, y=150)
    password_entry.insert(0, "Password")
    password_entry.bind("<FocusIn>", remove_password_placeholder)
    password_entry.bind("<FocusOut>", restore_password_placeholder)

    # Draw a line below the Input Text box
    Frame(signup_form_frame, width=295, height=2, bg="black").place(x=25, y=177)
    ##########----------------------------------------------------------------------
    ##########----------------------------------------------------------------------
    ##########----------------------------------------------------------------------

    # Remove the Password Confirmation input placeholder
    def remove_confirmation_password_placeholder(e):
        confirm_password_entry.delete(0, "end")

    # Restore the Password Confirmation input placeholder
    def restore_confirmation_password_placeholder(e):
        input_data = confirm_password_entry.get()
        if not input_data:
            confirm_password_entry.insert(0, "Confirm Password")

    # Confirmed Password text box
    confirm_password_entry = Entry(
        signup_form_frame,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Consolas", 11),
    )
    confirm_password_entry.place(x=30, y=220)
    confirm_password_entry.insert(0, "Confirm Password")
    confirm_password_entry.bind(
        "<FocusIn>", remove_confirmation_password_placeholder
    )
    confirm_password_entry.bind(
        "<FocusOut>", restore_confirmation_password_placeholder
    )

    # Draw a line below the Input Text box
    Frame(signup_form_frame, width=295, height=2, bg="black").place(x=25, y=247)
    ##########----------------------------------------------------------------------

    # Register button
    signup_button = Button(
        signup_form_frame,
        width=39,
        pady=7,
        text="Sing up",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=signup,
    )
    signup_button.place(x=35, y=280)

    # Option to by pass registry and log-in directy
    have_account_label = Label(
        signup_form_frame,
        text="You have an account?",
        fg="black",
        bg="white",
        font=("consolas", 9),
    )
    have_account_label.place(x=65, y=340)

    # Button to try log-in directy in sign up window
    signin_button = Button(
        signup_form_frame,
        width=6,
        text="Sing in",
        border=0,
        bg="white",
        cursor="hand2",
        fg="#57a1f8",
        command=open_signin_window,
    )
    signin_button.place(x=200, y=340)

    # Keep sign up window going
    signup_window.mainloop()
    ##
    ##
    ##
    ##
    ##


# Images for the window
# img = PhotoImage(file="signin.png") # Descomentar esta linea si se tiene la imagen
# signup_window_decoration = Label(signin_window, image=img, bg="white") # Descomentar esta linea si se tiene la imagen
signin_window_decoration = Label(
    signin_window, bg="blue"
)  # Borrar esta linea si se tiene la imagen
signin_window_decoration.place(x=50, y=50)

# Background of the form
signin_form_frame = Frame(signin_window, width=350, height=390, bg="#fff")
signin_form_frame.place(x=480, y=50)

# Visible title of the form
signin_form_heading = Label(
    signin_form_frame,
    text="Sign in",
    fg="#57a1f8",
    bg="white",
    font=("Consolas", 23, "bold"),
)
signin_form_heading.place(x=100, y=5)

##########----------------------------------------------------------------------

# Remove the Username input placeholder
def remove_username_placeholder(e):
    username_entry.delete(0, "end")


# Restore the Username input placeholder
def restore_username_placeholder(e):
    input_data = username_entry.get()
    if not input_data:
        username_entry.insert(0, "Username")


# Username text box
username_entry = Entry(
    signin_form_frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Consolas", 11),
)
username_entry.place(x=30, y=80)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", remove_username_placeholder)
username_entry.bind("<FocusOut>", restore_username_placeholder)

# Draw a line below the Input Text box
Frame(signin_form_frame, width=295, height=2, bg="black").place(x=25, y=107)
##########----------------------------------------------------------------------
##########----------------------------------------------------------------------

# Remove the Password input placeholder
def remove_password_placeholder(e):
    password_entry.delete(0, "end")


# Restore the Password input placeholder
def restore_password_placeholder(e):
    input_data = password_entry.get()
    if not input_data:
        password_entry.insert(0, "Password")


# Password text box
password_entry = Entry(
    signin_form_frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Consolas", 11),
)
password_entry.place(x=30, y=150)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", remove_password_placeholder)
password_entry.bind("<FocusOut>", restore_password_placeholder)

# Draw a line below the Input Text box
Frame(signin_form_frame, width=295, height=2, bg="black").place(x=25, y=177)
##########----------------------------------------------------------------------

################################################################################

# Log in button
sigin_button = Button(
    signin_form_frame,
    width=39,
    pady=7,
    text="Sing in",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=signin,
)
sigin_button.place(x=35, y=208)

# Option to scape log in and go to register
donthave_account_label = Label(
    signin_form_frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("consolas", 9),
)
donthave_account_label.place(x=55, y=270)

# Button to try sign up directy from sign in window
signup_button = Button(
    signin_form_frame,
    width=6,
    text="Sing up",
    border=0,
    bg="white",
    cursor="hand2",
    fg="#57a1f8",
    command=open_signup_window,
)
signup_button.place(x=215, y=270)

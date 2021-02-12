from tkinter import *

def register():
    username_info = username.get()
    password_info = password.get()


    file = open(username_info + "_login.txt","w")
    file.write("Username: "+username_info +"\n")
    file.write("Password: "+password_info)
    file.close()

    username_entry.delete(0, "end")
    password_entry.delete(0, "end")

    Label(screen0, text = "Registration success", fg = "green", font = ("arial", 13)).pack()

def sign_in():
    global screen0
    screen0 = Toplevel(screen)
    screen0.title("sign in")
    screen0.geometry=(300,250)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen0, text = "Please, enter your informations below.").pack()
    Label(screen0, text = "").pack()
    Label(screen0, text = "Username").pack()
    username_entry = Entry(screen0, textvariable = username)
    username_entry.pack()
    Label(screen0, text = "Password").pack()
    password_entry = Entry(screen0, textvariable = password)
    password_entry.pack()
    Label(screen0, text = "").pack()
    Button(screen0, text = "Sign in", width = 10, height = 1, command = register).pack()


def login():
    print("Login session stared!")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry=(300,250)
    screen.title("Register System")
    Label(text = "Register", bg = "gray", width="50", height="3", font = ("arial", 13)).pack()
    Label(text = " ").pack()
    Button(text = "login", height = "2", width = "30", command = login).pack()
    Label(text = " ").pack()
    Button(text = "Sing in", height = "2", width = "30", command = sign_in).pack()

    screen.mainloop()

main_screen()
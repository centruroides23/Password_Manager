from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_comp = [choice(letters) for letter in range(randint(8, 10))]
    symbols_comp = [choice(symbols) for symbol in range(randint(2, 4))]
    numbers_comp = [choice(numbers) for number in range(randint(2, 4))]

    password_list = letters_comp + symbols_comp + numbers_comp
    shuffle(password_list)

    password = "".join(password_list)
    pass_ent.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = web_ent.get()
    try:
        with open("passwords.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=web_ent.get(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Information Error", message=f"No Details for the {website} Exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_ent.get()
    email = user_ent.get()
    password = pass_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(web_ent.get()) == 0 or len(pass_ent.get()) == 0:
        messagebox.showerror(title="Error in Password", message="No password was entered. Please, enter a password.")
    else:
        try:
            with open("passwords.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_ent.delete(0, END)
            pass_ent.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website:", font=("Arial", 10, "normal"))
web_lab.grid(column=0, row=1)
user_lab = Label(text="Email/Username:", font=("Arial", 10, "normal"))
user_lab.grid(column=0, row=2)
pass_lab = Label(text="Password:", font=("Arial", 10, "normal"))
pass_lab.grid(column=0, row=3)

web_ent = Entry(width=33)
web_ent.focus()
web_ent.grid(column=1, row=1)
user_ent = Entry(width=52)
user_ent.insert(0, "oscar.bejarano503@gmail.com")
user_ent.grid(column=1, row=2, columnspan=2)
pass_ent = Entry(width=33)
pass_ent.grid(column=1, row=3)

pass_but = Button(text="Generate Password", command=generate_password)
pass_but.grid(column=2, row=3)
add_but = Button(width=44, text="Add", command=save)
add_but.grid(column=1, row=4, columnspan=2)
search_but = Button(text="Search", width=14, command=find_password)
search_but.grid(column=2, row=1, columnspan=2)


window.mainloop()
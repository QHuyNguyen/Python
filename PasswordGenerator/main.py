import tkinter
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #for char in range(nr_letters):
    #  password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for char in range(nr_letters)]

    #for char in range(nr_symbols):
    #  password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    print(password_list)
    password = "".join(password_list)
    #for char in password_list:
    #  password += str(char)

    print(f"Your password is: {password}")
    password_textbox.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_stuff():
    website_entry = website_textbox.get()
    email_entry = email_textbox.get()
    password_entry = password_textbox.get()
    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(message='need to enter shit in')
    elif messagebox.askokcancel(title=website_entry, message=f'{email_entry} | {password_entry}'):
        generate_file(website_entry, email_entry, password_entry)

def generate_file(website_entry, email_entry, password_entry):
    with open(file='text_file.txt', mode='a') as file:
        file.write(f'{website_entry} | {email_entry} | {password_entry}\n')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text='Website: ')
website_label.grid(column=0, row=1)
website_textbox = tkinter.Entry(width=35)
website_textbox.grid(column=1, row=1, columnspan=2)
website_textbox.focus()

email_label = tkinter.Label(text='Email/Username: ')
email_label.grid(column=0, row=2)
email_textbox = tkinter.Entry(width=35)
email_textbox.grid(column=1, row=2, columnspan=2)
email_textbox.insert(0, 'random@gmail.com')

password_label = tkinter.Label(text='Pasword: ')
password_label.grid(column=0, row=3)
password_textbox = tkinter.Entry(width=21)
password_textbox.grid(column=1, row=3)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = tkinter.Button(text='Add', width=36, command=add_stuff)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
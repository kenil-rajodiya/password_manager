from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import pyperclip
from json import *
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    new_data = {
        website_input.get():{
            "email":user_input.get(),
            "password":password_input.get()
        }
    }
    if len(website_input.get())==0 or len(user_input.get())==0 or len(password_input.get())==0:
        messagebox.showerror(title="Empty field",message="enter all fields")
    else:
        is_ok=messagebox.askokcancel(title=website_input.get(),message=f"These are details entered :\nEmail: {user_input.get()}\nPassword: {password_input.get()}\n is it ok?")
        if is_ok:
            try:
                with open("data.json", "r") as dfile:
                    data=load(dfile)
                    # print(data)
            except FileNotFoundError:
                with open("data.json","w") as dfile:
                    dump(new_data,dfile,indent=4)

            else:
                data.update(new_data)
                with open("data.json","w")as dfile:
                    dump(data,dfile,indent=4)
            finally:
                website_input.delete(0, END)
                user_input.delete(0,END)
                password_input.delete(0,END)







# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = [random.choice(letters) for _ in range(nr_letters)]
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
password_list+=[random.choice(symbols) for _ in range(nr_symbols)]
password_list+=[random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

def generate_password():
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)


def find_password():
    finder=website_input.get()
    try:
        with(open("data.json","r")as d_file):
            data1=load(d_file)

        try:
            messagebox.showinfo(title="Details",message=f"Email:{data1[finder]['email']}\nPassword:{data1[finder]['password']}")
        except KeyError:
            messagebox.showerror(message="No data found")
    except FileNotFoundError:
        print("Empty file")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=220, height=209)
window.config(padx=50, pady=50)
img = PhotoImage(file="logo.png")
cnv = Canvas(highlightthickness=0, height=200, width=200)
cnv.create_image(100, 100, image=img)
cnv.grid(row=0, column=1)

website_label = Label(text="Website:", pady=5)
website_input = Entry(width=32)
website_label.grid(row=1, column=0, padx=5)
website_input.focus()
website_input.grid(row=1, column=1, pady=5)


search_button=Button(text="Search",command=find_password,width=13)
search_button.grid(row=1,column=2,pady=5)



user_label = Label(text="Email/Username:", pady=5)
user_input = Entry(width=51)
user_label.grid(row=2, column=0, padx=5)
user_input.grid(row=2, column=1, columnspan=2, pady=5)

password_label = Label(text="Password:", pady=5)
password_input = Entry(width=32)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, pady=5)

password_generate_button = Button(text="Generate Password", pady=5,command=generate_password)
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, pady=5, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

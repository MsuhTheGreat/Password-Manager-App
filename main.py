import tkinter as tk
from tkinter import ttk, END, messagebox
from random import randint, choice
import pyperclip
import os
import subprocess
import json

directory_path = "D:\\Usman_Programming\\Usman_Projects\\Hundered_Days_of_Code_by_Angela_Yu\\Project_26_Password_Manager_App\\"

with open(directory_path + "seven_zip_path.txt", mode="r") as file:
    seven_zip_path = file.read()

# -------------------------------- DECRYPT FILE ------------------------------------- #
def decrypt():
    if not os.path.exists(directory_path + "Passwords.7z"):
        with open(directory_path + "Passwords.json", mode="w") as file:
            data = {}
            json.dump(data, file, indent=4)
        return
    try:
        subprocess.run([seven_zip_path, "e", f"-p{password}", directory_path + "Passwords.7z", "-y"], check=True)
    except Exception as e:
        ask = messagebox.askokcancel(title="Password Decrypter", message=f"Error Occurred: {e}")
        encrypt()
        if ask:
            exit(0)
        else:
            exit(0)

# ---------------------------------- ENCRYPT FILE ----------------------------------- #
def encrypt():
    try:
        subprocess.run([seven_zip_path, "a", "-t7z", f"-p{password}", "-mhe", directory_path + "Passwords.7z", directory_path + "Passwords.json", "-y"], check=True)
    except Exception as e:
        ask = messagebox.askokcancel(title="Password Encrypter", message=f"Error Occurred: {e}")
        if ask:
            exit(0)
        else:
            exit(0)
    else:
        os.remove(directory_path + "Passwords.json")

# -------------------------------- PASSWORD GENERATION ------------------------------ #
def generate_password():
    password_character_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','0','1','2','3','4','5','6','7','8','9','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','[',']',';',':','\\','|',',','<','.','>','/','?']
    character_length = randint(30, 40)
    password = ""
    i = 0
    while i < character_length:
        password += choice(password_character_list)
        i += 1
    password_entry.insert(END, password)

# ----------------------------------- SAVING PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username_email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Password Adder", message="You left a field behind. Please fill Website, Username/Email and Password fields!")
    else:
        user_agree = messagebox.askyesno(title="Password Adder", message=f"Do you want to add the following details to Passwords file?\nWebsite: {website}\nUsername/Email: {username_email}\nPassword: {password}")
        if user_agree:
            if os.path.exists(directory_path + "Passwords.7z"):
                decrypt()
            
            new_data = {website.capitalize(): {"Username/Email": username_email, "Password": password}}
            try:
                with open(directory_path + "Passwords.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = ""
            finally:
                data.update(new_data)
                with open(directory_path + "Passwords.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                
            pyperclip.copy(password)
            messagebox.showinfo(title="Password Adder", message="Your provided details have been successfully added to Passwords file. Your password has also been added to the clipboard. Paste it using Ctrl + V. Enjoy!")
            encrypt()
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# --------------------------------- SHOW PASSWORDS ---------------------------------- #
def show_passwords():
    decrypt()
    with open(directory_path + "Passwords.json", mode="r") as file:
        data = json.load(file)
    messagebox.showinfo(title="Password Viewer", message=json.dumps(data, indent=2))
    encrypt()

# -------------------------------- SEARCH PASSWORD ---------------------------------- #
def search_password():
    website = website_entry.get().capitalize()
    decrypt()
    with open(directory_path + "Passwords.json", mode="r") as file:
        data = json.load(file)
    if website in data:
        email = data[website]["Username/Email"]
        password = data[website]["Password"]
        pyperclip.copy(password)
        messagebox.showinfo(title="Password Viewer", message=f"Website: {website}\nUsername: {email}\nPassword: {password}\nYour password has been copied to the clipboard. Use Ctrl + V to paste it. Enjoy!")
    else:
        messagebox.showwarning(title="Password Viewer", message="No such website name found in the database!")
    encrypt()
# ------------------- PROMPT PASSWORD ENTRY OR CREATION ----------------------------- #
def on_closing_window():
    messagebox.showinfo(title="Password Manager", message="You cannot continue without entering password")
    exit(0)

if os.path.exists(directory_path + "Passwords.7z"):
    password_prompt_window = tk.Tk()
    password_prompt_window.title("Open the lock please!")
    password_prompt_window.config(padx=100, pady=50)

    canvas = tk.Canvas(password_prompt_window, width=230, height=230, highlightthickness=0)
    logo = tk.PhotoImage(file=directory_path + "opening_key.png")
    canvas.create_image(115, 115, image=logo)
    canvas.grid(row=0, column=1)

    message = "\nPlease open the lock using your created key!\n"
    label = ttk.Label(password_prompt_window, font=("Arial", 15, "italic"), text=message)
    label.grid(row=1, column=1)

    entry = ttk.Entry(password_prompt_window, width=40, font=("Arial", 15, "italic"), show="*")
    entry.grid(row=2, column=1)

    password = ""
    def check_password():
        global password
        password = entry.get()
        try:
            decrypt()
        except Exception as e:
            ask = messagebox.askokcancel(title="Password Checker", message=f"An Error Occurred: {e}")
            if ask:
                exit(0)
            else:
                exit(0)    
        else:
            encrypt()
            password_prompt_window.destroy()
        
    check_password_button = ttk.Button(password_prompt_window, text="Check Password", command=check_password)
    check_password_button.grid(row=3, column=1)

    password_prompt_window.protocol("WM_DELETE_WINDOW", on_closing_window)

    password_prompt_window.mainloop()
else:
    password_created = False
    while not password_created:
        password_generation_window = tk.Tk()
        password_generation_window.title("Generate a key")
        password_generation_window.config(padx=100, pady=50)

        canvas = tk.Canvas(password_generation_window, width=200, height=200, highlightthickness=0)
        key = tk.PhotoImage(file=directory_path + "key.png")
        canvas.create_image(100, 100, image=key)
        canvas.grid(row=1, column=1)

        message = "Create a strong key so that it will\nnot break by ordinary hammer strokes!\nYour key will be only in your pocket.\nKeep it safe!"
        text = ttk.Label(width=30, font=("Arial", 15, "italic"), text=message)
        text.config(padding=5)
        text.grid(row=2, column=1)

        key_entry = ttk.Entry(password_generation_window, width=30, font=("Arial", 15, "italic"), show="*")
        key_entry.grid(row=3, column=1)

        another_message = ttk.Label(width=30, font=("Arial", 15, "italic"), text="Copy from above and paste below.")
        another_message.config(padding=5)
        another_message.grid(row=4, column=1)

        enter_again_entry = ttk.Entry(password_generation_window, width=30, font=("Arial", 15, "italic"), show="*")
        enter_again_entry.grid(row=5, column=1)

        def create_password():
            if key_entry.get() == enter_again_entry.get():
                global password, password_created
                password = key_entry.get()
                password_created = True
                try:
                    decrypt()
                except Exception as e:
                    ask = messagebox.askokcancel(title="Password Checker", message=f"An Error Occurred: {e}")
                    if ask:
                        exit(0)
                    else:
                        exit(0)    
                else:
                    encrypt()
                    password_generation_window.destroy()
            else:
                password_generation_window.destroy()
                messagebox.showwarning(title="Password Generator", message="Enter the same password in both fields.")
            
        create_password_button = ttk.Button(password_generation_window, width=55, text="Create The Key", command=create_password)
        create_password_button.grid(row=6, column=1)

        password_generation_window.protocol("WM_DELETE_WINDOW", on_closing_window)

        password_generation_window.mainloop()

# ---------------------------------- UI SETUP --------------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file=directory_path + "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = ttk.Label(window, text="Website:", font=("Arial", 15, "bold"))
website_label.grid(row=1, column=0)
website_label.config(padding=5)

username_email_label = ttk.Label(window, text="Username/Email:", font=("Arial", 15, "bold"))
username_email_label.grid(row=2, column=0)
username_email_label.config(padding=5)

password_label = ttk.Label(window, text="Password:", font=("Arial", 15, "bold"))
password_label.grid(row=3, column=0)
password_label.config(padding=5)

website_entry = ttk.Entry(window, width=22, font=("Arial", 15, "italic"))
website_entry.focus()
website_entry.grid(row=1, column=1)

username_email_entry = ttk.Entry(window, width=40, font=("Arial", 15, "italic"))
username_email_entry.insert(string="m.usmantwpsc@gmail.com", index=0)
username_email_entry.grid(row=2, column=1, columnspan=2)

password_entry = ttk.Entry(window, width=22, font=("Arial", 15, "italic"))
password_entry.grid(row=3, column=1)

search_password_button = ttk.Button(window, width=31, text="Search Password", command=search_password)
search_password_button.grid(row=1, column=2)

generate_password_button = ttk.Button(window, width=31, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_password_button = ttk.Button(window, width=73, text="Add Password", command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)

view_passwords_button = ttk.Button(window, width=73, text="View Passwords", command=show_passwords)
view_passwords_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
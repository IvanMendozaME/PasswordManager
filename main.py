from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pswd_letters = [choice(letters) for i in range(randint(0,10))]
    pswd_symbols = [choice(symbols) for i in range(randint(2,4))]
    pswd_numbers = [choice(numbers) for i in range(randint(2,4))]
    pswd_list = pswd_letters + pswd_symbols + pswd_numbers
    shuffle(pswd_list)
    password = "".join(pswd_list)

    print(f"Your password is: {password}")
    evalue.set("")
    entryPswd.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    WB = entryWebSite.get()
    EM = entryEmail.get()
    PSW = entryPswd.get()

    if WB == "" or PSW == "":
        messagebox.showinfo(title="WAWRNING", message="Please, complete the fiels")
    
    else:
        isOk = messagebox.askyesnocancel(title=WB, message=f"These are the details entered: \nEmail: {EM}"
                                                f"\nPawwrod: {PSW} \nIs it ok to save?")

        if isOk:
            with open("data.txt", "a") as file:
                dataInsert = f"{WB} | {EM} | {PSW} \n"
                file.write(dataInsert)
            file.close()
            entryWebSite.delete(0,END)
            entryPswd.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

#Layers
Timer = Label(text="Website:")
Timer.grid(column=0,row=1)
Timer = Label(text="Email/Username: ")
Timer.grid(column=0,row=2)

Timer = Label(text="Password: ")
Timer.grid(column=0,row=3)

#Entries
entryWebSite = Entry(width=53)
entryWebSite.grid(column=1,row=1,columnspan=2, sticky="w")
entryWebSite.focus()
entryEmail = Entry(width=53)
entryEmail.grid(column=1,row=2,columnspan=2, sticky="w")
entryEmail.insert(0,"ivan@gmail.com")
evalue = StringVar()
entryPswd = Entry(width=33, textvariable=evalue)
entryPswd.grid(column=1,row=3, sticky="w")

#Buttons
Gnrt_PSWD = Button(text="Generate Password", command=generate)
Gnrt_PSWD.grid(column=2, row=3, columnspan=2)

Add = Button(text="Add", width=45, command=save)
Add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
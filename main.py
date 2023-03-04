import tkinter as tk
import random
import pyperclip
import string

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Password Generator")
        self.resizable(False, False)
        self.geometry("430x150")

        mainframe = tk.Frame(self, padx=5, pady=5)
        mainframe.grid(column=0, row=0, sticky="NWES")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ENTRY
        str_var = tk.StringVar()
        self.pwd_entry = tk.Entry(mainframe, width=25, textvariable=str_var)
        self.pwd_entry.grid(column=1, row=1, sticky="NWES")
        x = "".join(random.choice(list(string.ascii_lowercase)) for _ in range(10))
        str_var.set(x)

        # COPY BUTTON
        copy_button = tk.Button(mainframe, text="Copy Password", command=self.copy)
        copy_button.grid(column=1, row=4)

        # LABEL
        pwd_length_label = tk.Label(mainframe, text="Password length:")
        pwd_length_label.grid(column=0, row=2, sticky="WES")

        # SCALE
        str_var = tk.StringVar(value=10)
        self.pwd_length_scale = tk.Scale(mainframe, from_=1, to=50, orient="horizontal",variable=str_var, command=self.generate)
        self.pwd_length_scale.grid(column=1, row=2, sticky="NWES")

        # creating frame for photos and placing it in mainframe
        self.photo_frame = tk.Frame(mainframe)
        self.photo_frame.grid(column=2, row=1)

        # PHOTO REPEAT
        self.photo1 = tk.PhotoImage(file="repeat_icon.png")
        self.generate_button_repeat = tk.Button(self.photo_frame, image=self.photo1, compound="right", command=self.generate)
        self.generate_button_repeat.grid(column=1, row=1, sticky="W")

        #PHOTO COPY
        self.photo2 = tk.PhotoImage(file="copy_icon.png")
        self.generate_button_copy = tk.Button(
            self.photo_frame, image=self.photo2, compound="right", command=self.copy
            )
        self.generate_button_copy.grid(column=0, row=1, sticky="W")

        # creating frame for check buttons and placing it in mainframe
        self.check_frame = tk.Frame(mainframe)
        self.check_frame.grid(column=1, row=3)

        # CHECKBUTTONS
        self.lower = tk.BooleanVar(value=True)
        self.upper = tk.BooleanVar()
        self.numbers = tk.BooleanVar()
        self.symbol = tk.BooleanVar()

        check_lower = tk.Checkbutton(self.check_frame, text="abc", variable=self.lower, command=lambda:[self.update_checkbox(), self.generate()])
        check_upper = tk.Checkbutton(self.check_frame, text="ABC", variable=self.upper, command=lambda: [self.update_checkbox(), self.generate()])
        check_number = tk.Checkbutton(self.check_frame, text="123", variable=self.numbers, command=lambda: [self.update_checkbox(), self.generate()])
        check_symbols = tk.Checkbutton(self.check_frame, text="#$&", variable=self.symbol, command=lambda: [self.update_checkbox(), self.generate()])

        check_lower.grid(column=0, row=3)
        check_upper.grid(column=1, row=3)
        check_number.grid(column=2, row=3)
        check_symbols.grid(column=3, row=3)

        
    def generate(self, *args):
        """Generates password depends which checboxes are checked."""
        lower_alphabet = list(string.ascii_lowercase)
        upper_alphabet = list(string.ascii_uppercase)
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
        current_list = []
        password = []
        
        if self.lower.get():
            current_list.extend(lower_alphabet)
        if self.upper.get():
            current_list.extend(upper_alphabet)
        if self.numbers.get():
            current_list.extend(digits)
        if self.symbol.get():
            current_list.extend(symbols)

        for _ in range(self.pwd_length_scale.get()):
            password.append(random.choice(current_list))

        self.pwd_entry.delete(0, tk.END)
        self.pwd_entry.insert(0, "".join(password))
        return "".join(password)


    def update_checkbox(self):
        """Checks if any checkbox is unchecked and if so then checks the first checkbox"""
        if self.upper.get() == 0 and self.numbers.get() == 0 and self.symbol.get() == 0:
            self.lower.set(True)

    
    def copy(self):
        pyperclip.copy(self.pwd_entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()

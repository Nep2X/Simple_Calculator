import tkinter as tk
from tkinter import ttk
import customtkinter

class App():

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.mainframe = customtkinter.CTkFrame(self.root, fg_color="light blue")
        self.mainframe.pack(fill='both', expand=True)

        self.actTitle = customtkinter.CTkLabel(self.mainframe, text="SIMPLE CALCULATOR", font=("Unispace", 25))
        self.actTitle.place(relx=0.3, rely=0.05)
        self.name = customtkinter.CTkLabel(self.mainframe, text="By: Neftali Tinambing LFCA211M042", font=("Unispace", 12))
        self.name.place(relx=0.32, rely=0.1)

        # Number Buttons
        self.one = customtkinter.CTkButton(self.mainframe, text="1", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("1"))
        self.one.place(relx=0.1, rely=0.34)
        self.two = customtkinter.CTkButton(self.mainframe, text="2", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("2"))
        self.two.place(relx=0.28, rely=0.34)
        self.three = customtkinter.CTkButton(self.mainframe, text="3", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("3"))
        self.three.place(relx=0.45, rely=0.34)
        self.four = customtkinter.CTkButton(self.mainframe, text="4", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("4"))
        self.four.place(relx=0.1, rely=0.56)
        self.five = customtkinter.CTkButton(self.mainframe, text="5", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("5"))
        self.five.place(relx=0.28, rely=0.56)
        self.six = customtkinter.CTkButton(self.mainframe, text="6", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("6"))
        self.six.place(relx=0.45, rely=0.56)
        self.seven = customtkinter.CTkButton(self.mainframe, text="7", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("7"))
        self.seven.place(relx=0.1, rely=0.78)
        self.eight = customtkinter.CTkButton(self.mainframe, text="8", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("8"))
        self.eight.place(relx=0.28, rely=0.78)
        self.nine = customtkinter.CTkButton(self.mainframe, text="9", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("9"))
        self.nine.place(relx=0.45, rely=0.78)
        self.zero = customtkinter.CTkButton(self.mainframe, text="0", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("0"))
        self.zero.place(relx=0.63, rely=0.78)

        # Operator Buttons
        self.add = customtkinter.CTkButton(self.mainframe, text="+", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("+"))
        self.add.place(relx=0.63, rely=0.34)
        self.minus = customtkinter.CTkButton(self.mainframe, text="-", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("-"))
        self.minus.place(relx=0.8, rely=0.34)
        self.multi = customtkinter.CTkButton(self.mainframe, text="*", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("*"))
        self.multi.place(relx=0.63, rely=0.56)
        self.dev = customtkinter.CTkButton(self.mainframe, text="/", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("/"))
        self.dev.place(relx=0.8, rely=0.56)

        # Other Buttons
        self.delete = customtkinter.CTkButton(self.mainframe, text="C", width=100, height=100, font=("Unispace", 50), command=self.clear_input)
        self.delete.place(relx=0.8, rely=0.13)
        self.equal = customtkinter.CTkButton(self.mainframe, text="=", width=100, height=100, font=("Unispace", 50), command=self.calculate_result)
        self.equal.place(relx=0.8, rely=0.78)

        # Input Textbox
        self.input1 = customtkinter.CTkTextbox(self.mainframe, font=("Unispace", 35), width=445, height=70, border_color="black", border_width=5)
        self.input1.place(relx=0.1, rely=0.19)
        self.input1.configure(state="disabled")  # Disable direct typing

        self.root.mainloop()

    def update_input(self, value):
        self.input1.configure(state="normal")  # Enable editing
        self.input1.insert("end", value)  # Append the number/operator
        self.input1.configure(state="disabled")  # Disable direct typing

    def clear_input(self):
        self.input1.configure(state="normal")
        self.input1.delete("0.0", "end")
        self.input1.configure(state="disabled")

    def calculate_result(self):
        self.input1.configure(state="normal")
        expression = self.input1.get("0.0", "end").strip()  # Get input
        try:
            result = eval(expression)  # Evaluate the expression
            self.input1.delete("0.0", "end")
            self.input1.insert("0.0", str(result))  # Display result
        except Exception as e:
            self.input1.delete("0.0", "end")
            self.input1.insert("0.0", "Error")
        self.input1.configure(state="disabled")

if __name__ == '__main__':
    App()

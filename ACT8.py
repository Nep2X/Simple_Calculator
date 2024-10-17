import tkinter as tk
from tkinter import ttk
import customtkinter

class App():

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    def __init__ (self):

        self.root = tk.Tk()
        self.root.geometry('650x500')
        self.root.title("NepNep's Simple Calculator")
        self.mainframe = customtkinter.CTkFrame(self.root, fg_color="#433878")
        self.mainframe.pack(fill='both', expand=True)

        self.actTitle = customtkinter.CTkLabel(self.mainframe, text="SIMPLE CALCULATOR", font=("Unispace", 25), text_color="white")
        self.actTitle.place(relx=0.3, rely=0.05)
        self.name = customtkinter.CTkLabel(self.mainframe, text="By: Neftali Tinambing LFCA211M042", font=("Unispace", 12), text_color="white")
        self.name.place(relx=0.32, rely=0.1)

        self.one = customtkinter.CTkButton(self.mainframe, text="1", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("1"), fg_color="#7E60BF")
        self.one.place(relx=0.09, rely=0.34)
        self.two = customtkinter.CTkButton(self.mainframe, text="2", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("2"), fg_color="#7E60BF")
        self.two.place(relx=0.26, rely=0.34)
        self.three = customtkinter.CTkButton(self.mainframe, text="3", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("3"), fg_color="#7E60BF")
        self.three.place(relx=0.43, rely=0.34)
        self.four = customtkinter.CTkButton(self.mainframe, text="4", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("4"), fg_color="#7E60BF")
        self.four.place(relx=0.09, rely=0.56)
        self.five = customtkinter.CTkButton(self.mainframe, text="5", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("5"), fg_color="#7E60BF")
        self.five.place(relx=0.26, rely=0.56)
        self.six = customtkinter.CTkButton(self.mainframe, text="6", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("6"), fg_color="#7E60BF")
        self.six.place(relx=0.43, rely=0.56)
        self.seven = customtkinter.CTkButton(self.mainframe, text="7", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("7"), fg_color="#7E60BF")
        self.seven.place(relx=0.09, rely=0.78)
        self.eight = customtkinter.CTkButton(self.mainframe, text="8", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("8"), fg_color="#7E60BF")
        self.eight.place(relx=0.26, rely=0.78)
        self.nine = customtkinter.CTkButton(self.mainframe, text="9", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("9"), fg_color="#7E60BF")
        self.nine.place(relx=0.43, rely=0.78)
        self.zero = customtkinter.CTkButton(self.mainframe, text="0", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("0"), fg_color="#7E60BF")
        self.zero.place(relx=0.61, rely=0.78)


        self.add = customtkinter.CTkButton(self.mainframe, text="+", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("+"), fg_color="#7E60BF")
        self.add.place(relx=0.61, rely=0.34)
        self.minus = customtkinter.CTkButton(self.mainframe, text="-", width=100, height=100, font=("Unispace", 50),  command=lambda: self.update_input("-"), fg_color="#7E60BF")
        self.minus.place(relx=0.78, rely=0.34)
        self.multi = customtkinter.CTkButton(self.mainframe, text="*", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("*"), fg_color="#7E60BF")
        self.multi.place(relx=0.61, rely=0.56)
        self.dev = customtkinter.CTkButton(self.mainframe, text="/", width=100, height=100, font=("Unispace", 50), command=lambda: self.update_input("/"), fg_color="#7E60BF")
        self.dev.place(relx=0.78, rely=0.56)

        self.delete = customtkinter.CTkButton(self.mainframe, text="C", width=100, height=100, font=("Unispace", 50), command=self.clear_input, fg_color="#7E60BF")
        self.delete.place(relx=0.78, rely=0.13)
        self.equal = customtkinter.CTkButton(self.mainframe, text="=", width=100, height=100, font=("Unispace", 50), command=self.calculate_result, fg_color="#7E60BF")
        self.equal.place(relx=0.78, rely=0.78)

        self.input1 = customtkinter.CTkTextbox(self.mainframe, font=("Unispace", 35), width=435, height=70, border_color="#7E60BF", border_width=5)
        self.input1.place(relx=0.1, rely=0.19)

          
        self.root.mainloop()
    
    def update_input(self, value):
        self.input1.configure(state="normal")
        self.input1.insert("end", value)
        self.input1.configure(state="disabled")

    def clear_input(self):
        self.input1.configure(state="normal")
        self.input1.delete("0.0", "end")
        self.input1.configure(state="disabled")

    def calculate_result(self):
        self.input1.configure(state="normal")
        expression = self.input1.get("0.0", "end").strip()
        try:
            result = eval(expression)
            self.input1.delete("0.0", "end")
            self.input1.insert("0.0", str(result))
        except Exception as e:
            self.input1.delete("0.0", "end")
            self.input1.insert("0.0", "Error")
        self.input.configure(state="disabled")

    



    

if __name__ == '__main__':
    App()

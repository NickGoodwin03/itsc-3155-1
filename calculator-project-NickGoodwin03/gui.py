from scientific_calc import ScientificCalculator
from tkinter import *


class CalcGUI():

    def __init__(self):
        # Frame initialization parameters
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("250x200")
        self.root.config(bg="#c5c8e0")

        # Result window
        self.resultwindow = Entry(self.root, borderwidth=2, relief=SUNKEN)
        self.resultwindow.grid(row=0, column=4, columnspan=6, pady=5)
        self.resultwindow.config(font=("Terminal", 12))

        # Label for the drop down menu
        self.label = Label(
            self.root, text="Operator", font=("Terminal", 12))
        self.label.grid(row=1, column=0, columnspan=2, pady=5)
        self.label.config(font=("Terminal", 12), bg="#c5c8e0")

        # Operation dropdown menu
        self.operation = StringVar()
        self.operation.set("+")  # default value
        self.operationmenu = OptionMenu(
            self.root, self.operation, "+", "-", "*", "/", "^", "%", "!", "sin", "cos", "tan", "ln")
        self.operationmenu.grid(row=1, column=4, columnspan=2, pady=5)
        self.operationmenu.config(font=("Terminal", 12))

        # Text entry box for first number
        self.num1 = Entry(self.root, borderwidth=2, relief=SUNKEN)
        self.num1.grid(row=2, column=4, columnspan=2, pady=5, padx=5)
        self.num1.config(font=("Terminal", 12))
        self.num1.focus_set()
        self.num1.insert(0, "0")

        # Label for the first number, set to the left of the text entry box
        self.num1label = Label(self.root, text="Number 1")
        self.num1label.grid(row=2, column=0, columnspan=2, pady=5)
        self.num1label.config(font=("Terminal", 12), bg="#c5c8e0")

        # Text entry box for second number
        self.num2 = Entry(self.root, borderwidth=2, relief=SUNKEN)
        self.num2.grid(row=3, column=4, columnspan=2, pady=5, padx=5)
        self.num2.config(font=("Terminal", 12))
        self.num2.insert(0, "0")

        # Label for the second number, set to the left of the text entry box
        self.num2label = Label(self.root, text="Number 2")
        self.num2label.grid(row=3, column=0, columnspan=2, pady=5)
        self.num2label.config(font=("Terminal", 12), bg="#c5c8e0")

        # Button to calculate the result
        self.calc = Button(self.root, text="Calculate", command=self.calculate)
        self.calc.grid(row=4, column=4, columnspan=2, pady=5)
        self.calc.config(font=("Terminal", 12))

        # Button to quit
        self.quit = Button(self.root, text="Quit", command= self.root.destroy)
        self.quit.grid(row=5, column=4, columnspan=2, pady=5)
        self.quit.config(font=("Terminal", 12))

        self.root.mainloop()

    def calculate(self):

        # Creating a scientific calculator object, which will perform the calculations
        Sci_Cal = ScientificCalculator()

        # Get methods here are grabbing values from the GUI object
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())

        # Need to use new different method to grab/assign our operator
        operator = self.operation.get()
        Sci_Cal.operation = operator

        # Assigns values to the Sci_Cal objects num1 and num2 attributes
        Sci_Cal.set_num1(num1)
        Sci_Cal.set_num2(num2)

        # Calls the Sci_Cal object's sci_calculate method
        Sci_Cal.sci_calculate()

        self.resultwindow.delete(0, END)
        self.resultwindow.insert(0, Sci_Cal.get_result())


if __name__ == "__main__":
    CalcGUI()

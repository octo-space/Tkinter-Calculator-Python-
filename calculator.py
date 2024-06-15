from tkinter import Tk, Entry, Button, StringVar

class Calculator():
    def __init__(self, master):
        master.title("--  Simple Calculator --")
        master.geometry('350x420+0+0')  # Set window geometry

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=16, bg='#fff', font=('Arial Bold', 25), textvariable=self.equation).place(x=0, y=0, width=350, height=50)

        # Row 1
        Button(width=11, height=4, text='(',  relief='flat', bg="white", command=lambda: self.show('(')).place(x=0, y=60, width=80, height=50)
        Button(width=11, height=4, text=')',  relief='flat', bg="white", command=lambda: self.show(')')).place(x=90, y=60, width=80, height=50)
        Button(width=11, height=4, text='%',  relief='flat', bg="white", command=lambda: self.show('%')).place(x=180, y=60, width=80, height=50)
        Button(width=11, height=4, text='/',  relief='flat', bg="white", command=lambda: self.show('/')).place(x=270, y=60, width=80, height=50)

        # Row 2
        Button(width=11, height=4, text='7',  relief='flat', bg="white", command=lambda: self.show(7)).place(x=0, y=120, width=80, height=50)
        Button(width=11, height=4, text='8',  relief='flat', bg="white", command=lambda: self.show(8)).place(x=90, y=120, width=80, height=50)
        Button(width=11, height=4, text='9',  relief='flat', bg="white", command=lambda: self.show(9)).place(x=180, y=120, width=80, height=50)
        Button(width=11, height=4, text='*',  relief='flat', bg="white", command=lambda: self.show('*')).place(x=270, y=120, width=80, height=50)

        # Row 3
        Button(width=11, height=4, text='4',  relief='flat', bg="white", command=lambda: self.show(4)).place(x=0, y=180, width=80, height=50)
        Button(width=11, height=4, text='5',  relief='flat', bg="white", command=lambda: self.show(5)).place(x=90, y=180, width=80, height=50)
        Button(width=11, height=4, text='6',  relief='flat', bg="white", command=lambda: self.show(6)).place(x=180, y=180, width=80, height=50)
        Button(width=11, height=4, text='-',  relief='flat', bg="white", command=lambda: self.show('-')).place(x=270, y=180, width=80, height=50)

        # Row 4
        Button(width=11, height=4, text='1',  relief='flat', bg="white", command=lambda: self.show(1)).place(x=0, y=240, width=80, height=50)
        Button(width=11, height=4, text='2',  relief='flat', bg="white", command=lambda: self.show(2)).place(x=90, y=240, width=80, height=50)
        Button(width=11, height=4, text='3',  relief='flat', bg="white", command=lambda: self.show(3)).place(x=180, y=240, width=80, height=50)
        Button(width=11, height=4, text='+',  relief='flat', bg="white", command=lambda: self.show('+')).place(x=270, y=240, width=80, height=50)

        # Row 5
        Button(width=11, height=4, text='c',  relief='flat', bg="white", command=self.clear).place(x=0, y=300, width=80, height=50)
        Button(width=11, height=4, text='0',  relief='flat', bg="white", command=lambda: self.show(0)).place(x=90, y=300, width=80, height=50)
        Button(width=11, height=4, text='.',  relief='flat', bg="white", command=lambda: self.show('.')).place(x=180, y=300, width=80, height=50)
        Button(width=11, height=4, text='=',  relief='flat', bg="white", command=self.solve).place(x=270, y=300, width=80, height=50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("Error")


root = Tk()
calculator = Calculator(root)
root.mainloop()

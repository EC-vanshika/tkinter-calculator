from tkinter import *
import ast

def get_number(num):
    display.insert(END, str(num))

def get_operation(operator):
    current = display.get()
    if current and current[-1] in '+-*/%':
        display.delete(len(current)-1, END)
    display.insert(END, operator)

def clear_all():
    display.delete(0, END)

def calculate():
    try:
        result = eval(compile(ast.parse(display.get(), mode="eval"), '<string>', 'eval'))
        clear_all()
        display.insert(END, str(result))
    except:
        clear_all()
        display.insert(END, "error")

def undo():
    current = display.get()
    display.delete(len(current)-1, END)

root = Tk()
root.title("Tkinter Calculator")

display = Entry(root, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
display.grid(row=0, column=0, columnspan=4, pady=10)

# Layout for buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('AC',5,0), ('<-',5,1), ('(',5,2), (')',5,3)
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'AC':
        cmd = clear_all
    elif text == '<-':
        cmd = undo
    elif text in '+-*/()':
        cmd = lambda t=text: get_operation(t)
    else:
        cmd = lambda t=text: get_number(t)

    Button(root, text=text, width=5, height=2, font=("Arial",14), command=cmd).grid(row=row, column=col, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()

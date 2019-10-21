import tkinter as tk
from tkinter import *
  
    
# tkinter call
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600+300+300")
root.resizable(0,0)


data = StringVar()
val = ""
a = 0
operator = ""


# Label
lbl = Label(
    root, text="label",
    anchor=SE,
    font=("Verdana", 30),
    textvariable = data,
    bg = "#ffffff",
    fg = "#000000"

)

lbl.pack(expand=True, fill="both")


###FUNCTIONS###
# Clicked 1
def click_1():
    global val
    val = val + "1"
    data.set(val)

# Clicked 2
def click_2():
    global val
    val = val + "2"
    data.set(val)

# Clicked 3
def click_3():
    global val
    val = val + "3"
    data.set(val)

# Clicked 4
def click_4():
    global val
    val = val + "4"
    data.set(val)

# Clicked 5
def click_5():
    global val
    val = val + "5"
    data.set(val)

# Clicked 6
def click_6():
    global val
    val = val + "6"
    data.set(val)

# Clicked 7
def click_7():
    global val
    val = val + "7"
    data.set(val)

# Clicked 8
def click_8():
    global val
    val = val + "8"
    data.set(val)

# Clicked 9
def click_9():
    global val
    val = val + "9"
    data.set(val)

# Clicked 0
def click_0():
    global val
    val = val + "0"
    data.set(val)

# Clicked -
def click_sub():
    global a
    global operator
    global val
    a = int(val),
    operator = "-"
    val = val + "-"
    data.set(val)
 
# Clicked x
def click_into():
    global a
    global operator
    global val
    a = int(val),
    operator = "x"
    val = val + "x"
    data.set(val)

# Clicked /
def click_div():
    global a
    global operator
    global val
    a = int(val),
    operator = "/"
    val = val + "/"
    data.set(val)

# Clicked +
def click_add():
    global a
    global operator
    global val
    a = int(val),
    operator = "+"
    val = val + "+"
    data.set(val)
    
# Clicked C
def click_C():
    global a
    global val
    global operator
    val = ""
    a = 0
    operator = ""
    data.set(val)

# Clicked Equals
def result():
    global a
    global operator
    global val
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = a + x
        data.set(C)
        val = StringVar(C)
        print(x)
# Button row 1
btn_row1 = Frame(root)
btn_row1.pack(
    expand = True,
    fill = "both"
)

# Button row 2
btn_row2 = Frame(root)
btn_row2.pack(
    expand = True,
    fill = "both"
)

# Button row 3
btn_row3 = Frame(root)
btn_row3.pack(
    expand = True,
    fill = "both"
)

# Button row 4
btn_row4 = Frame(root)
btn_row4.pack(
    expand = True,
    fill = "both"
)

# Button row 5
btn_row5 = Frame(root)
btn_row5.pack(
    expand=True,
    fill="both"
)




# Number One
button1 = tk.Button(
    btn_row1,
    text="1",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_1,
)

button1.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)


# Number Two
button2 = tk.Button(
    btn_row1,
    text="2",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_2,
)

button2.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)




# Number Three
button3 = tk.Button(
    btn_row1, text="3",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_3,
)

button3.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)




# Number Four
button4 = tk.Button(
    btn_row2,
    text="4",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_4,
)

button4.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)



# Number Five
button5 = tk.Button(
    btn_row2,
    text="5",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_5,
)

button5.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)


# Number Six
button6 = tk.Button(
    btn_row2,
    text="6",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_6,
)
button6.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)




# Number Seven
button7 = tk.Button(
    btn_row3,
    text="7",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_7,
)

button7.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)



# Number Eight
button8 = tk.Button(
    btn_row3,
    text="8",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_8,
)

button8.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)


# Number Nine
button9 = tk.Button(
    btn_row3,
    text="9",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_9,
)

button9.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)

# Clear Button
buttonC = tk.Button(
    btn_row4,
    text="C",
    padx=10,
    pady=10,
    font=("Verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_C
)

buttonC.pack(
    side = LEFT,
    expand=True,
    fill="both"
)

# Number Zero
button0 = tk.Button(
    btn_row4,
    text="0",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_0,
)

button0.pack(
    side = RIGHT,
    expand = True,
    fill = "both"
)



# Equals Button
buttondot = tk.Button(
    btn_row4,
    text="=",
    padx=10,
    pady=10,
    font=("Verdana", 25),
    relief = GROOVE,
    border = 0,
    command = result,
)

buttondot.pack(
    side = LEFT,
    expand=True,
    fill="both"
)



# Addition button
sum_button = tk.Button(
    btn_row5,
    text="+",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_add,
)

sum_button.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)



# Subtraction button
minus_button = tk.Button(
    btn_row5,
    text="-",
    padx=10,
    pady=10,
    command=click_sub,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
)

minus_button.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)



# Multiplication button
multiplication_button = tk.Button(
    btn_row5,
    text="x",
    padx=10,
    pady=10,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
    command = click_into,
)

multiplication_button.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)



# Divide button
division_button = tk.Button(
    btn_row5,
    text="/",
    padx=10,
    pady=10,
    command=click_div,
    font = ("verdana", 25),
    relief = GROOVE,
    border = 0,
)

division_button.pack(
    side = LEFT,
    expand = True,
    fill = "both"
)


root.mainloop()

from random import randrange
import tkinter as tk

i = 0
repeat = 10
heads = 0
tails = 0
flipped = 0
root = tk.Tk()
root.title('Coin Flipper it Is') 
root.configure()
label = tk.Label(
    root,
    text = 'How many times do you want to flip the coin?   -->',
    height = 3,
    width = 39, 
) .grid(
    row = 0,
    column = 0,
)

Enter_num = tk.Entry(
    root,
    textvariable = repeat,
) .grid(
    row = 0,
    column = 1,
)
 
def flipper():
    global i 
    global heads
    global tails
    global flipped
    global repeat
    while i <= repeat:
        flip = randrange(2)
        if flip %2 == 0:
            heads += 1
            flipped += 1
            print(repeat)
        else:
            tails += 1
            flipped += 1
            print(repeat)
        i += 1
        return heads and tails and flipped


button = tk.Button(
    root,
    text = 'FLIP!',
    bg = 'white',
    fg = 'black',
    command = on()
) .grid(
    row = 0,
    column = 2,
)
root.mainloop()



        


def hangman():
    pass


def jj(event):
    hangman()




from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk
wordlist = ['soham', 'pushpak', 'pranav', 'ojas', 'aryan']




#---------------------------------------------------------------------------------------------------Main_window
master = Tk()
master.geometry('800x500+300+100')
# master.configure(bg='SteelBlue1')
icon_image = PhotoImage(file='hangman_icon.png')
master.iconphoto(False, icon_image)
master.title('The Hangman game')
master.focus_force()

# ------------------------------------------------------------CANVAS creation for main window
canvas = Canvas(master, width=800, height=500)
canvas.pack(fill="both", expand=True)

main_bg_image = Image.open("background_image5.jpg")
main_bg_image = main_bg_image.resize((800, 500))
main_bg = ImageTk.PhotoImage(main_bg_image)

bg_label = Label(master, image=main_bg)
canvas.create_image(0, 0, image=main_bg, anchor="nw")
bg_label.pack()

# ------------------------------------------------------------------------------Labels
# intro_label = Label(master, text="Welcome to Hangman Game", bg='SteelBlue1', font=('Segoe Script', 25, 'bold'))
# intro_label.place(x=170, y=10)

canvas.create_text(400, 50, text="Welcome to Hangman Game", font=('Segoe Script', 30, 'bold'), fill='white')

# word_label = Label(master, text='* * * *', justify='center', font=('arial', 60), bg='SteelBlue1', fg='black')
# word_label.place(x=300, y=150)

canvas.create_text(400, 230, text='', font=('arial', 60), fill='black')

# left_chances = Label(master, text='Left = 4', font=('Bahnschrift', 20), bg='SteelBlue1', fg='black')
# left_chances.place(x=700, y=450)

canvas.create_text(700, 450,  text='Left = 4', font=('Bahnschrift', 20), fill='white')

ans = Label(master, text='', font=('Bahnschrift', 20), bg='SteelBlue1', fg='black')
ans.place(x=345, y=430)

# ------------------------------------------------------------------------------Entry Box
inpp = StringVar()
input1 = Entry(master, relief='sunken', font=('arial', 25, 'bold'), justify='center', bg='light sky blue', textvariable=inpp)
input1.place(x=230, y=250)
input1.focus_set()

#------------------------------------------------------------------------------------Button
bt1 = Button(master, relief='raise', text='Submit', font=('Bahnschrift', 25, 'bold'), bg='RoyalBlue4',
                 activeforeground='tomato', command=hangman)
# bt1.focus_set()
bt1.place(x=345, y=350)
master.bind("<Return>",jj)
#-------------------------------------------------------------------------------------------------------

def show_main_win():
    master.deiconify()


#------------------------------------------start_window
new_window = Toplevel(master)
new_window.geometry('800x500+300+100')
# new_window.configure(bg='SteelBlue1')
p1 = PhotoImage(file='hangman_icon.png')
new_window.iconphoto(False, p1)
new_window.title('The Hangman game')

# ----------------------------------------------CANVAS creation for top level window
canvas1 = Canvas(new_window, width=800, height=500)
canvas1.pack(fill="both", expand=True)


bg_image = Image.open("background_image.jpg")
bg_image = bg_image.resize((800, 500))
bg_image_f = ImageTk.PhotoImage(bg_image)

# bg_label =Label(new_window, image=bg_image_f)
canvas1.create_image(0, 0, image=bg_image_f, anchor="nw")
# bg_label.pack()



# master.withdraw()
# st_label = Label(new_window, text="Hangman Game", font=("Amperzand", 50, 'bold'))
# st_label.place(x=180, y=100)

canvas1.create_text(450, 100, text="Hangman Game", font=("Gill Sans MT", 50))
canvas1.create_text(450, 180, text="Guessing words consists of the names of team\n\tmembers and colours", font=('arial', 20, 'italic'), fill='white')

bt = Button(new_window, text='Start', font=('Birch Std', 30, 'bold'), bg='tomato', command=show_main_win)
bt.focus_set()
bt.place(x=350, y=300)


master.mainloop()
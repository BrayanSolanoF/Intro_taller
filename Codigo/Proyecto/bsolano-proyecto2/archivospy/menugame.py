from tkinter import *
import tkinter as tk
from mainnew import *

def connect():
    #menu.iconify()
    menu.destroy()

    pg.init()
    g = Game()
    #g.show_start_screen()
    #g.name
    #g.inpt()
    while True:
        g.new()
        g.run()
        g.show_go_screen()

def save():
    import json as serializer
    with open('godhelpme.txt', 'w') as f:
        serializer.dump(username.get(), f)
    # with open('some_file.txt', 'w') as f:
    #     serializer.dump(password.get(), f)
    #menu.quit()

menu = tk.Tk()
menu.title("DEATH RACE")
menu.geometry("1024x768")
imagen = PhotoImage(file="viper.png")
#imgbtn = PhotoImage(file ="boton.png")
fondo = Label(menu,image=imagen).place(x=0,y=0)

Label(menu, text ="Username").grid(row = 0)
#Label(menu, text ="Password").grid(row = 1)

username = StringVar()
#password = StringVar()

e1 = Entry (menu, textvariable=username)
#e2 = Entry (menu, textvariable=password, show= "*")

e1.grid(row = 0, column = 1)
#e2.grid(row = 1, column = 1)

# changed "command"
button1 = Button(menu, text = "Register", command = save)
button2 = Button(menu, text='Salir', command=menu.quit, height = 4, width = 20).place(x=435,y=400)
connectPygame = Button(menu, text='Play', command=connect,height = 4, width = 20).place(x=435,y=200)
button1.grid(columnspan = 2)
button1.bind("<Button-1>")
menu.mainloop()
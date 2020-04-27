import tkinter
import random

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text="Случайное слово")
label.pack()
a = {'which': 'который', 'were': 'были', 'dog': 'собака'}
var = tkinter.StringVar()
ser = tkinter.StringVar()
var.set(random.choice(list(a.keys())))
label = tkinter.Label(frame, textvariable=var)
label.pack()

label = tkinter.Label(frame, text="Укажите перевод слова:")
label.pack()
entry = tkinter.Entry(frame)
entry.pack()
def ygad():
    if entry.get() == a[var.get()]:
        ser.set('Угадали')
        var.set(random.choice(list(a.keys())))
    else:
        ser.set('Неугадали')

ser.set('Я верю  в тебя')

label = tkinter.Label(frame, textvariable=ser)
label.pack()


button = tkinter.Button(frame, text='Готово', command=ygad)
button.pack()

button = tkinter.Button(frame, text='Выход', command =exit)
button.pack()


window.mainloop()
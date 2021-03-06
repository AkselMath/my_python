import tkinter
import json
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text='Задача:')
label.grid(row=1, column=1)

entry1 = tkinter.Entry(frame)
entry1.grid(row=1,column=2)

label = tkinter.Label(frame, text='Категория:')
label.grid(row=2, column=1)

entry2 = tkinter.Entry(frame)
entry2.grid(row=2,column=2)

label = tkinter.Label(frame, text='Время:')
label.grid(row=3, column=1)

entry3 = tkinter.Entry(frame)
entry3.grid(row=3,column=2)

def zadat():
    with open('js.json', 'r') as file:
        data = json.load(file)
    data.update( {counter.get(): {'task ': entry1.get(), 'category': entry2.get(), 'time': entry3.get() } } )

    with open('js.json', 'w') as f:
        json.dump(data, f)

    counter.set(counter.get() + 1)

counter = tkinter.IntVar()
counter.set(1)

def spis():
    with open('js.json', 'r') as file:
        data = json.load(file)
    print(data)

button = tkinter.Button(frame, text='Задать', command = zadat)
button.grid(row=4,column=2)

button = tkinter.Button(frame, text='Список задач', command = spis)
button.grid(row=5,column=2)

button = tkinter.Button(frame, text='Выход', command = exit)
button.grid(row=6,column=2)


window.mainloop()
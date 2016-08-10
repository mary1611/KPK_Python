import tkinter

def paint(event):
    """ Обработчик событий для холста
    :param event: событие
    :return: ничего
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print('Странно, ведь paint()привязывали только к Canvas..')
        return
    canvas.coords(line, 0, 0, event.x, event.y)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, bg='white', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0,0,10, 10)
for i in range(10):
    canvas.create_oval(i*40, i*40, i*40+30, i*40+30, fill='green', width=2)
    
root.mainloop()
print ("это будет только при выходе из виджета")

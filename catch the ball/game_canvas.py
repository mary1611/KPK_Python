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
    canvas.coords(line, 0, 0, event_x, event_y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root)
canvas.bird("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0,0,10, 10)

root.mainloop()
print ("это будет только при выходе из виджета")
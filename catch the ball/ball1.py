import tkinter


def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие
    :return: ничего
    По клику мышкой нужно удалять тот объект, на который указывает мышка
    А также засчитывать очки польз-ля
    """


def create_random_ball():
    canvas.create_oval(x,y,x+2*R, y+2*R, width=1, fill=random_color())
    """
    Создает шарик в случайном месте игрового холста canvas
    ппри этом шарик не выходит за границы холста
    """

def init_ball_catch_game():
    """
    Создает необх для игры ко-во шариков по ктр надо кликать
    """

def init_main_windows():
    global root, canvas

root = tkinter.Tk()



root.mainloop()


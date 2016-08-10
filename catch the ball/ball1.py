import tkinter
from random import choice, randint

ball_initial_number = 50
ball_minimal_radius = 15
ball_maximal_radius = 45
ball_avaliable_color = ['green', 'blue', 'red','lightgrey',
                        '#FF00FF', '#FFFF00']


def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие
    :return: ничего
    По клику мышкой нужно удалять тот объект, на который указывает мышка
    А также засчитывать очки польз-ля
    """
    obj=canvas.find_closest(event.x,event.y)
    x1,y1,x2,y2 = canvas.coors(obj)
    
    if x1 <= event.x <= x2 and y1 <= event.y <=y2:
        canvas.delete(obj)
        #FIXME:учитываем объект в очках
        create_random_ball()

def move_all_balls(event):
    """
    :return: передвигает все шарики не далеко
    """
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj, dx, dy)


def create_random_ball():
    R=randint(ball_minimal_radius, ball_minimal_radius)
    x=randint(0,int.canvas['width']-1-R)
    y=randint(0,int.canvas['height']-1-R)
    canvas.create_oval(x,y,x+2*R, y+2*R, width=1, fill=random_color())
    """
    Создает шарик в случайном месте игрового холста canvas
    ппри этом шарик не выходит за границы холста
    """


def random_color():
    """
    :return:Случайный цвет из некоторого набора цветов
    """
    return choice(ball_avaliable_color)


def init_ball_catch_game():
    """
    Создает необх для игры ко-во шариков по ктр надо кликать
    """
    for i in range(ball_initial_number):
        create_random_ball()
        

def init_main_window():
    global root, canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background='white',
                            width=400,height=400)
    canvas.bind("<Button>",click_ball)
    canvas.bind("<Motion>")
    canvas.pack()

    for i in range(10):

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("давайте ещё поиграем")
    


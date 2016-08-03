from turtle import turtle

def init_drawman():
    global t, x_current, y_current
    t - Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current,y_current)
    drawman_scale = 10

def test_drawman():
    """
    тестироание работы Чертёжника
    :return:None
    """
    pen_down()
    for i in range(8):
        on_vector(10,20)
        on_vector(0,-20)
    pen_up()
    to_point(0,0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx,dy):
    to_point(x_current + dx, y_current + dy )

def to_point(x,y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(drawman_scale*x_current, drawman_scale*y_current)

init_drawman()
if _name_ =='_main_':
    import time
    test_drawman()
    time.sleep()

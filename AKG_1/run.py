# -*- coding: utf-8 -*-

from tkinter import *
from calc_proj import *
import time
from threading import Thread

color = 'blue'
back_color = 'white'
size_line = 60


def show_figure(points, color='black', title_numbers=False):
    '''
    points_tmp = []
    for i in range(len(points)):
        x = points[i].X
        y = points[i].Y
        points_tmp.append([x,y])
    my_tuple = tuple(points_tmp)
    canvas.create_polygon(my_tuple, width=3, fill='red')
    #canvas.create_polygon(my_tuple, width=3, outline=color, fill='red')
    '''
    count = len(points)
    i = 0
    while i < count-1:
        if title_numbers:
            canvas.create_text(points[i].X+10, points[i].Y+10, text=i+1, fill=color)
        canvas.create_line(points[i].X, points[i].Y, points[i+1].X, points[i+1].Y, fill=color, width=3)
        i += 1
    if title_numbers:
        canvas.create_text(points[count-1].X + 10, points[count-1].Y + 10, text=count, fill=color)
    canvas.create_line(points[count-1].X, points[count-1].Y, points[0].X, points[0].Y, fill=color, width=3)
    return True
    

def draw_figures(start_figure, finish_figure, title_numbers=False):
    show_figure(start_figure, color, title_numbers)
    show_figure(finish_figure, color, title_numbers)


def draw_motion(morphing, start_figure, finish_figure):
    for i in range(steps.get()):
        if not show_history.get():
            show_figure(morphing.get_current_coord(start_figure, finish_figure, i-1, steps.get()), back_color)
        show_figure(morphing.get_current_coord(start_figure, finish_figure, i, steps.get()), color)
        draw_figures(start_figure, finish_figure)
        canvas.update()
        time.sleep(var_timeout.get())
        if not show_history.get():
            show_figure(morphing.get_current_coord(start_figure, finish_figure, steps.get()-1, steps.get()), back_color)
            draw_figures(start_figure, finish_figure)


class ThreadDraw():
    def __init__(self, morphing, start_figure, finish_figure):
        self.th = Thread(target=draw_motion, args=(morphing, start_figure, finish_figure))
    def run(self):
        self.th.start()


def draw_morphing(event):
    canvas.delete('all')
    morphing = Morphing()
    morphing.size = size_line
    morphing.start_count_figure = var_start_figure.get()
    morphing.finish_count_figure = var_finish_figure.get()
    start_figure = morphing.get_coord_start_figure()
    finish_figure = morphing.get_coord_finish_figure()
    draw_figures(start_figure, finish_figure)
    th = ThreadDraw(morphing, start_figure, finish_figure)
    th.run()


def clear_canvas(event):
    canvas.delete('all')
    canvas.update()
    morphing = Morphing()
    morphing.size = size_line
    morphing.start_count_figure = var_start_figure.get()
    morphing.finish_count_figure = var_finish_figure.get()
    start_figure = morphing.get_coord_start_figure()
    finish_figure = morphing.get_coord_finish_figure()
    draw_figures(start_figure, finish_figure)
    return True


root = Tk()
root.title('АКГ. Лабороторная работа 1')
root.resizable(0,0)
root.geometry('1000x600+100+100')

canvas = Canvas(root, width=800, height=600)
canvas.configure(background=back_color)
canvas.pack(side='left')

frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

frame_buttons = Frame(frame)
frame_buttons.pack()

button = Button(frame_buttons, text='Start')
button.bind('<Button-1>', draw_morphing)
button.pack(padx=5, pady=5, side='left')

clear_button = Button(frame_buttons, text='Clear')
clear_button.bind('<Button-1>', clear_canvas)
clear_button.pack(padx=5, pady=5, side='right')

frame_settings = LabelFrame(frame, text='Settings')
frame_settings.pack(fill=BOTH, expand=1)

show_history = BooleanVar()
show_history.set(False)
check = Checkbutton(frame_settings, text='Show history', variable=show_history)
check.pack()

frame_timeout = Frame(frame_settings)
frame_timeout.pack()

label_timeout = Label(frame_timeout, text='Timeout: ')
label_timeout.pack(padx=5, pady=5, side='left')

var_timeout = DoubleVar()
timeout_entry = Entry(frame_timeout, textvariable=var_timeout)
var_timeout.set(0.1)
timeout_entry.pack(padx=5, pady=5, side='right')

frame_start_figure_settings = Frame(frame_settings)
frame_start_figure_settings.pack()

label_start_figure = Label(frame_start_figure_settings, text='Start figure: ')
label_start_figure.pack(padx=5, pady=5, side='left')

var_start_figure = IntVar()
start_figure_entry = Entry(frame_start_figure_settings, textvariable=var_start_figure)
var_start_figure.set(6)
start_figure_entry.pack(padx=5, pady=5, side='right')

frame_finish_figure_settings = Frame(frame_settings)
frame_finish_figure_settings.pack()

label_finish_figure = Label(frame_finish_figure_settings, text='Finish figure: ')
label_finish_figure.pack(padx=5, pady=5, side='left')

var_finish_figure = IntVar()
finish_figure_entry = Entry(frame_finish_figure_settings, textvariable=var_finish_figure)
var_finish_figure.set(3)
finish_figure_entry.pack(padx=5, pady=5, side='right')

frame_steps_setting = Frame(frame_settings)
frame_steps_setting.pack()

label_steps = Label(frame_steps_setting, text='Steps: ')
label_steps.pack(padx=5, pady=5, side='left')

steps = IntVar()
steps_entry = Entry(frame_steps_setting, textvariable=steps)
steps.set(30)
steps_entry.pack(padx=5, pady=5, side='right')


root.mainloop()

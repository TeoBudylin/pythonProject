from time import sleep
from itertools import cycle
from tkinter import *
from multiprocessing import Process


class TrafficLight:
    __colors = ("red", "yellow", "green", "yellow")
    def __init__(self):
        self.color ="red"

    def running(self):
        for light in cycle(self.__colors):
            print(self.color)
            if self.color == "red":
                sleep(7)
            elif self.color == "yellow":
                sleep(1)
            elif self.color == "green":
                sleep(4)
            self.color = light


trafficlight = TrafficLight()

trafficlight.running()


# root = Tk()
# root.title = "Trafficlight"
# root.geometry("300x300")
#
# canvas = Canvas(root)
# canvas.pack()
#
# def colors_loop():
#     __colors = ("red", "yellow", "green", "yellow")
#     for light in cycle(__colors):
#         sleep(2)
#         frame = Frame(root, bg=light)
#         frame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.7)
#
#
# p2 = Process(target=colors_loop())
# p1 = Process(target=root.mainloop())
#
# p2.start()
# p1.start()
#
# p1.join()
# p2.join()
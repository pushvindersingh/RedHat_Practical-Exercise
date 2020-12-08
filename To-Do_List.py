# ToDo List Program

# Importing libraries

import tkinter
import threading
from tkinter import messagebox
import sys

# Initialising few variables

tasks = []

watch = threading

actual_watch = threading

flag = True


def get_task(event = ""):
    
    obj = todo.get()

    hour = int(time.get())

    todo.delete(0, tkinter.END)

    time.delete(0, tkinter.END)

    todo.focus_set()

    add_task(obj, hour)

    if 0 < hour < 999:

        update_task()


def add_task(obj, hrs):

    tasks.append([obj, hrs])

    clock = threading.Timer(hrs, proceed_time, [obj])

    clock.start()


def update_task():
    
    if WorkingList.size() > 0:

        WorkingList.delete(0, "end")

    for task in tasks:

        WorkingList.insert("end", "" + task[0] + " =======>>> Time left: " + str(task[1]) + " Seconds")


def proceed_time(task):

    tkinter.messagebox.showinfo("Notification", "Its Now the Time for : " + task)


def actual_time():

    if flag:

        actual_watch = threading.Timer(1.0, actual_time)

        actual_watch.start()

    for task in tasks:

        if task[1] == 0:

            tasks.remove(task)

        task[1] -= 1

    update_task()


if __name__ == "__main__":

    # application

    root = tkinter.Tk()

    root.geometry("460x480")

    root.title("Students to do List Reminder")

    root.rowconfigure(0, weight=1)

    root.config(bg="aqua")
        
    frame = tkinter.Frame(root)
    
    frame.pack()
    
    # Designing various Widgets
        
    label = tkinter.Label(root, text="Enter Tasks To Do:", fg = "white", bg = "blue", 
                        font = ('Arial', 15), wraplength = 300)
    
    label_hours = tkinter.Label(root, text = "Enter time (in seconds)", fg = "white",
                            bg = "blue", font = ('Arial', 14), wraplength = 200)
    
    todo = tkinter.Entry(root, width = 30, font = ('Arial', 15))
    
    time = tkinter.Entry(root, width = 15, font = ('Arial', 15))
    
    post = tkinter.Button(root, text = "Add task", fg = "white", bg = "green",
                          font = ("Arial", 16), relief = "ridge", bd = 5, height = 3,
                          width = 30, command = get_task)
    
    exiting = tkinter.Button(root, text = 'Exit', fg = "white", bg = 'red', height = 3,
                          font = ('Arial Bold', 14), relief = "ridge", bd = 5, 
                          width = 30, command = root.destroy)
    
    WorkingList = tkinter.Listbox(root, font = ('Arial', 12))
    
    if tasks != "":
        actual_time()
    
    # Binding the root
    
    root.bind('<Return>', get_task)
    
    # Placing the Widgets
    
    label.place(x=0, y=10, width=200, height=25)
    
    label_hours.place(x=235, y=10, width=200, height=25)
    
    todo.place(x=20, y=40, width=160, height=25)
    
    time.place(x=245, y=40, width=170, height=25)
    
    post.place(x=62, y=80, width=100, height=25)
    
    exiting.place(x=302, y=80, width=50, height=25)
    
    WorkingList.place(x=20, y=120, width=395, height=300)
    
    root.mainloop()
    
    flag = False
    
    sys.exit("This Program is ended...Thank You !!")
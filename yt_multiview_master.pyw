import time
import os
import threading
try:
    from tkinter import *
except ModuleNotFoundError:
    os.system('pip install tkinter')

try:
    import pyautogui
except ModuleNotFoundError:
    os.system('pip install pyautogui')

try:
    from selenium import webdriver
except ModuleNotFoundError:
    os.system('pip install selenium')

try:
    from PIL import ImageTk
except ModuleNotFoundError:
    os.system('pip install pillow')


def open_window(driver_number, youtube_link):
    driver = webdriver.Firefox()
    extension_path = 'zenmate.xpi'
    driver.install_addon(extension_path)

    driver.get(youtube_link)
    driver.set_window_size(300, 400)

    driver.switch_to.window(driver.window_handles[1])
    driver.close()

    print(f'[+] Done for driver {driver_number}')

def done():
    global youtube_link, total_driver
    youtube_link = entry.get()
    total_driver = int(Spinbox1.get())
    
    # Create and start threads for opening windows
    threads = []
    for i in range(total_driver):
        t = threading.Thread(target=open_window, args=(i+1, youtube_link))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print('[+] All windows opened')


root = Tk()
root.title('YT auto view')
root.geometry('400x250')
root.resizable(False, False)

# main frame 
main_frame = LabelFrame(root)
main_frame.pack(padx=10, pady=20)

# seecond frame
xframe = Frame(main_frame)
xframe.grid(row=0, column=0)

# last frame
frame = Frame(xframe, width=300, height=200)
frame.grid(row=0, column=0)

# lable for Titel
lb = Label(frame, text="Enter youtube link")
lb.grid(row=0, column=0)

# Image with lable
icon_image = ImageTk.PhotoImage(file='yt30.png')
lable3 = Label(frame,image=icon_image)
lable3.place(x=240,y=-2)


lable4 = Label(frame,image=icon_image)
lable4.place(x=60,y=-2)

# Entry box for get youtube link
entry = Entry(frame, width=40)
entry.grid(row=1, column=0, padx=5, pady=5)

# lable2 for text
Label2 = Label(frame, text='How much window you want to open?').grid(row=2, column=0, padx=5, pady=5)

# Spinbox for get amount
Spinbox1 = Spinbox(frame, from_=1, to=30)
Spinbox1.grid(row=3, column=0, padx=10, pady=10)

# Button for start 
btn = Button(frame, text="Start", fg='#fff', bg='#1e1f20', font='Calibri 12', command=done)
btn.grid(row=4, column=0, padx=5, pady=5, sticky='news')

root.mainloop()



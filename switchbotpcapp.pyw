from io import StringIO
from tkinter import colorchooser
from tkinter import *
from tkinter import ttk
import subprocess
import pymsgbox
import getpass
import inspect
import sys
import os

user = getpass.getuser()        # get the name of the current user
devicespath = ('C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt' .format(user))          # set path for devices.txt

if not os.path.exists('C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt' .format(user)):     # write instructions to devices.txt, opening notepad, and hiding the file
    w = open(devicespath, 'w')
    w.write("""




Hello! Follow the instructions below!

1. Follow this tutorial to get your switchbot token : https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started
2. Open printdevices.py
3. On the first line of this file paste your switchbot token
   On the second line of this file paste the deviceId of your lights
   On the third line of this file paste the deviceId of your color bulb
4. Save the file and close this window

Tv support comming soon!
If you dont have some of the devices mentioned above , just leave the line empty!
    """)
    w.close()
    pymsgbox.alert('Close this popup and follow instructions!', 'First time opening detected!')
    os.system("notepad C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt".format(user))
    os.system("attrib +h C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt".format(user))

def resource_path(relative_path):     # gets the path of the temp folder
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

with open('C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt'.format(user)) as devices: # Read info from devices.txt
    devices = [line.rstrip() for line in devices]

def debug():        # Display Debug data, this shows if something isnt working
    print("Token : " , devices[0])
    print("LED Light Line : " , devices[1])
    print("Color Bulb Line : " , devices[2])
    print("Devices.txt File : " + resource_path("devices.txt"))
    print("Json Folder : " + resource_path("json"))
    print("Images Folder : " + resource_path("images"))

debug()

#==================================================================================================================================
def choose_color(): # function to open windows color selector and to writes that color to bulb_color.json
    color_code = colorchooser.askcolor(title ="Choose color")
    color_code = color_code[0]
    color_result_rgb = ' '.join(format(x, "1.0f") for x in color_code)
    color_code = color_result_rgb.replace(" ", ":")
    print('Bulb Color : ' + color_code)
    f = open(resource_path("json/bulb_color.json"), "w")
    f.write("""
    {
        "command": "setColor",
        "parameter": "%s",
        "commandType": "command"
    }
    """ % color_code)
    f.close()
    print(' Running function :',inspect.stack()[0][3])
def apply_brightness(): # function to get the number from 0-100 from scale "brightness" and send that info to the switchbot api
    print("Brightness : {}".format(brightness.get()))
    f = open(resource_path("json/bulb_brightness.json"), "w")
    f.write("""
    {
        "command": "setBrightness",
        "parameter": "%s",
        "commandType": "command"
    }
    """ % brightness.get())
    f.close()
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\bulb_brightness.json"),devices[2],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
#==================================================================================================================================
def led_mass_hide():
    brightness_up_button.place_forget()
    brightness_down_button.place_forget()
    box1.place_forget()
    red_button.place_forget()
    blue_button.place_forget()
    green_button.place_forget()
    purple_button.place_forget()
    box2.place(x=1, y=0)
    swap1_button.place(x=196, y=100)
    swap1_button.lift()

def led_mass_show():
    on_button.place(x=11, y=50)
    off_button.place(x=11, y=90)
    brightness_up_button.place(x=129, y=50)
    brightness_down_button.place(x=129, y=90)
    box1.place(x=1, y=0)
    red_button.place(x=11, y=150)
    blue_button.place(x=11, y=190)
    green_button.place(x=128, y=150)
    purple_button.place(x=128, y=190)
    swap1_button.place(x=196, y=250)
    swap1_button.lift()
    box2.place_forget()

def toggle1():
    global state1
    if state1 == "Hidden":
        led_mass_show()
        state1 = "Showing"
    elif state1 == "Showing":
        led_mass_hide()
        state1 = "Hidden"
#==================================================================================================================================
def bulb_mass_hide():
    box3.place_forget()
    choose_color.place_forget()
    apply_color_button.place_forget()
    brightness.place_forget()
    apply_brightness_button.place_forget()
    swap2_button.place(x=438, y=100)
    swap2_button.lift()
    box4.place(x=240, y=0)

def bulb_mass_show():
    box3.place(x=240, y=0)
    choose_color.place(x=368, y=90)
    apply_color_button.place(x=368, y=50)
    brightness.place(x=250, y=150)
    apply_brightness_button.place(x=250, y=200)
    swap2_button.place(x=438, y=250)
    swap2_button.lift()
    box4.place_forget()

def toggle2():
    global state2
    if state2 == "Hidden":
        bulb_mass_show()
        state2 = "Showing"
    elif state2 == "Showing":
        bulb_mass_hide()
        state2 = "Hidden"
#==================================================================================================================================
def settings_mass_hide():
    settings_button.config(image=settings_img)
    settings_button.image = settings_img
    box5.place_forget()
    devices_button.place_forget()
    show_debug_button.place_forget()
    text_box.place_forget()
    text_box.place_forget()
    state4 = "Hidden"

def settings_mass_show():
    settings_button.config(image=settings_show_img)
    settings_button.image = settings_show_img
    box5.place(x=10, y=383)
    devices_button.place(x=100, y=395)
    show_debug_button.place(x=100, y=450)
    show_debug_button.lift()
    settings_button.lift()
    text_box.place_forget()
    state4 = "Hidden"

def toggle3():
    global state3
    if state3 == "Hidden":
        settings_mass_show()
        state3 = "Showing"
    elif state3 == "Showing":
        settings_mass_hide()
        state3 = "Hidden"
#==================================================================================================================================
def toggle4():
    global state4
    if state4 == "Hidden":
        text_box.pack(expand=True)
        text_box.place(x=250, y=350)   
        state4 = "Showing"
    elif state4 == "Showing":
        text_box.place_forget()
        state4 = "Hidden"
#==============================================================================================================================
# When any of the functions are called they read from the first,second and third line of the devices.txt file and read from the files in the json folder and send all of that data to the switchbot api
def turn_on():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\on.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def turn_off():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\off.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def brightness_up():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\brightness_up.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def brightness_down():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\brightness_down.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def red():
    subprocess.call('curl -k -sS -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\red.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def blue():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\blue.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def green():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\green.json"),devices[1],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def purple():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\purple.json"),devices[1],devices[0]), shell=True)
#==================================================================================================================================
def turn_on2():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\on.json"),devices[2],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def turn_off2():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\off.json"),devices[2],devices[0]), shell=True)
    print(' Running function :',inspect.stack()[0][3])
def apply_color():
    subprocess.call('curl -k -X POST -H "Content-Type: application/json" -d @{} "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(resource_path("json\\bulb_color.json"),devices[2],devices[0]), shell=True)
#==================================================================================================================================
def open_devices():
    subprocess.call('notepad C:\\Users\\{}\\AppData\\Local\\Temp\\devices.txt'.format(user))
#==================================================================================================================================
# Specify title,icon,background,size of the window
window = Tk()

window.geometry('800x500')
window.title("Switchbot Pc App ( SPA )")
icon = PhotoImage(file=resource_path("images\\icon.png"))
window.iconphoto(False, icon)
window.configure(background='#192734')

#==================================================================================================================================
# This contains all of the buttons and images
settings_show_img=PhotoImage(file=resource_path("images\\settings_show.png"))
settings_img=PhotoImage(file=resource_path("images\\settings.png"))
settings_button = Button(window, highlightthickness=0, bd=0, text='', image=settings_img, command=toggle3)
settings_button.pack(ipadx=5, ipady=5, expand=True)
settings_button.place(x=10, y=450)
state3 = "Hidden"

box5_img = PhotoImage(file=resource_path("images\\settings_box.png"))
box5 = Canvas(window, width = 226, height = 107, highlightthickness=0, bd=0)
box5.create_image(0, 0, anchor=NW, image=box5_img) 

devices_img=PhotoImage(file=resource_path("images\\open_devices.png"))
devices_button = Button(window, highlightthickness=0, bd=0, text='', image=devices_img, command=lambda: open_devices())

show_debug_img=PhotoImage(file=resource_path("images\\show_debug.png"))
show_debug_button = Button(window, highlightthickness=0, bd=0, text='', image=show_debug_img, command=toggle4)
state4 = "Hidden"

text_box = Text(
    window,
    height=9,
    width=67
)
text_box.insert('end','''
Token : {}
LED Light Line : {}
Color Bulb Line : {}
Devices.txt File : {}
Json Folder : {}
Images Folder : {}
''' .format(devices[0],devices[1],devices[2],resource_path("devices.txt"),resource_path("json"),resource_path("images")))
text_box.config(state='disabled')

#==================================================================================================================================
box1_img = PhotoImage(file=resource_path("images\\box1.png"))
box1 = Canvas(window, width = 237, height = 287, highlightthickness=0, bd=0)
box1.create_image(0, 0, anchor=NW, image=box1_img) 

box2_img = PhotoImage(file=resource_path("images\\short1.png"))
box2 = Canvas(window, width = 237, height = 143, highlightthickness=0, bd=0)
box2.pack()
box2.place(x=1, y=0)
box2.create_image(0, 0, anchor=NW, image=box2_img) 

swap_img=PhotoImage(file=resource_path("images\\swap.png"))
swap1_button = Button(window, highlightthickness=0, bd=0, text='', image=swap_img, command=toggle1)
swap1_button.pack(ipadx=5, ipady=5, expand=True)
swap1_button.place(x=196, y=100)
state1 = "Hidden"

on_img=PhotoImage(file=resource_path("images\\on.png"))
on_button = Button(window, highlightthickness=0, bd=0, text='', image=on_img, command=lambda: turn_on())
on_button.pack(ipadx=5, ipady=5, expand=True)
on_button.place(x=11, y=50)

off_img=PhotoImage(file=resource_path("images\\off.png"))
off_button = Button(window, highlightthickness=0, bd=0, text='', image=off_img, command=lambda: turn_off())
off_button.pack(ipadx=5, ipady=5, expand=True)
off_button.place(x=11, y=90)

brightness_up_img=PhotoImage(file=resource_path("images\\brightness_up.png"))
brightness_up_button = Button(window, highlightthickness=0, bd=0, text='', image=brightness_up_img, command=lambda: brightness_up())

brightness_down_img=PhotoImage(file=resource_path("images\\brightness_down.png"))
brightness_down_button = Button(window, highlightthickness=0, bd=0, text='', image=brightness_down_img, command=lambda: brightness_down())

red_img=PhotoImage(file=resource_path("images\\red.png"))
red_button = Button(window, highlightthickness=0, bd=0, text='', image=red_img, command=lambda: red())

blue_img=PhotoImage(file=resource_path("images\\blue.png"))
blue_button = Button(window, highlightthickness=0, bd=0, text='', image=blue_img, command=lambda: blue())

purple_img=PhotoImage(file=resource_path("images\\purple.png"))
purple_button = Button(window, highlightthickness=0, bd=0, text='', image=purple_img, command=lambda: purple())

green_img=PhotoImage(file=resource_path("images\\green.png"))
green_button = Button(window, highlightthickness=0, bd=0, text='', image=green_img, command=lambda: green())

#==================================================================================================================================

box3_img = PhotoImage(file=resource_path("images\\box2.png"))
box3 = Canvas(window, width = 237, height = 287, highlightthickness=0, bd=0)
box3.create_image(0,0 , anchor=NW, image=box3_img)

box4_img = PhotoImage(file=resource_path("images\\short2.png"))
box4 = Canvas(window, width = 237, height = 143, highlightthickness=0, bd=0)
box4.pack()  
box4.place(x=240, y=0)
box4.create_image(0, 0, anchor=NW, image=box4_img) 

swap2_button = Button(window, highlightthickness=0, bd=0, text='', image=swap_img, command=toggle2)
swap2_button.pack(ipadx=5, ipady=5, expand=True)
swap2_button.place(x=438, y=100)
state2 = "Hidden"

choose_color_img=PhotoImage(file=resource_path("images\\choose_color.png"))
choose_color = Button(window, highlightthickness=0, bd=0, text='', image=choose_color_img, command = choose_color)

on2_img=PhotoImage(file=resource_path("images\\on.png"))
on2_button = Button(window, highlightthickness=0, bd=0, text='', image=on_img, command=lambda: turn_on2())
on2_button.pack(ipadx=5, ipady=5, expand=True)
on2_button.place(x=250, y=50)

off2_img=PhotoImage(file=resource_path("images\\off.png"))
off2_button = Button(window, highlightthickness=0, bd=0, text='', image=off_img, command=lambda: turn_off2())
off2_button.pack(ipadx=5, ipady=5, expand=True)
off2_button.place(x=250, y=90)

apply_color_img=PhotoImage(file=resource_path("images\\apply_color.png"))
apply_color_button = Button(window, highlightthickness=0, bd=0, text='', image=apply_color_img, command=lambda: apply_color())

brightness = Scale(window, from_=0, to=100, length=220, orient=HORIZONTAL, highlightthickness=0, bd=0)

apply_brightness_img=PhotoImage(file=resource_path("images\\apply_brightness.png"))
apply_brightness_button = Button(window, highlightthickness=0, bd=0, text='', image=apply_brightness_img, command=lambda: apply_brightness())

#==================================================================================================================================

window.mainloop()

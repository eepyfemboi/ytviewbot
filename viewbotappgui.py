from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import random
import time
import os
import random
import string
import colorama
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import threading, requests, ctypes, os, time, random, string
from datetime import datetime
from colorama import Fore, Style
import pyautogui
from tkinter import *

PATH = "C:\Perflogs\chromedriver.exe"

# Create window
window = Tk()
window.title("YouTube ViewBot Configuration(Test)")

# Create labels
url_label = Label(window, text="URL:")
url_label.grid(row=0, column=0)

hour_label = Label(window, text="Hours of each video to view:")
hour_label.grid(row=1, column=0)

minute_label = Label(window, text="Minutes of each video to view:")
minute_label.grid(row=2, column=0)

second_label = Label(window, text="Seconds of each video to view:")
second_label.grid(row=3, column=0)

count_label = Label(window, text="View Count:")
count_label.grid(row=4, column=0)

min_label = Label(window, text="Minimum Time Between Views:")
min_label.grid(row=5, column=0)

max_label = Label(window, text="Maximum Time Between Views:")
max_label.grid(row=6, column=0)

# Create input fields
url_entry = Entry(window, width=50)
url_entry.grid(row=0, column=1)

hour_entry = Entry(window, width=50)
hour_entry.grid(row=1, column=1)

minute_entry = Entry(window, width=50)
minute_entry.grid(row=2, column=1)

second_entry = Entry(window, width=50)
second_entry.grid(row=3, column=1)

count_entry = Entry(window, width=50)
count_entry.grid(row=4, column=1)

min_entry = Entry(window, width=50)
min_entry.grid(row=5, column=1)

max_entry = Entry(window, width=50)
max_entry.grid(row=6, column=1)

# Create button
def clicked():
    # Get user input
    url_list = url_entry.get().split(',')
    view_count = int(count_entry.get())
    min_time = int(min_entry.get())
    max_time = int(max_entry.get())

    # Convert time
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    second = int(second_entry.get())
    convminute = (int(hour)*60)+int(minute)
    convsecond = (int(convminute)*60)+int(second)

    # Open chrome
    driver = webdriver.Chrome(PATH)
    
    # Loop through list of videos
    for i in range(view_count):
        # Choose a random video
        random_url = random.choice(url_list)
        driver.get(random_url)

        # Wait specified amount of time
        time.sleep(convsecond)

        # Wait a random amount of time
        wait_time = random.randint(min_time, max_time)
        time.sleep(wait_time)

# Create button
submit_button = Button(window, text="Submit", command=clicked)
submit_button.grid(row=7, column=1)

# Add extra informatio
info0 = Label(window, text="When you click Submit, this will stop responding.")
info1 = Label(window, text="Please ignore it and do not close the window.")
info0.grid(row=8, column=1)
info1.grid(row=9, column=1)

# Run the window
window.mainloop()

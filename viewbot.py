import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Perflogs\chromedriver.exe"

amount = 0

os.system(f"title Youtube View Bot ^| Views Sent: {amount}")

# Getting the url and view count
url = input("Enter Video URL: ")
count = input("Enter View Count: ")

# Depreciated
"""
#my temporary fix to not have to figure out the exact number of seconds long the video is
hour = input("Please input video length in hours. If this does not apply, please just enter 0: ")
minute = input("Please input video length in minutes. If this does not apply, please just enter 0: ")
second = input("Please input video length in seconds: ")

convminute = (int(hour)*60)+int(minute)
convsecond = (int(convminute)*60)+int(second)
"""

# Getting the interval
time_1 = input("Enter Minimum Time Between Views in seconds: ")
time_2 = input("Enter Maximum Time Between Views in seconds: ")

# Defining a function to always get a random number as the interval
def get_interval():
    global time_1, time_2
    return random.randrange(int(time_1), int(time_2))

# Initializing the window
driver = webdriver.Chrome(PATH)

# Opening the video
driver.get(url)

# Waiting for the page to load
time.sleep(5)

# Getting the duration
duration_raw = driver.find_element(
    by = By.XPATH, 
    value = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[33]/div[2]/div[1]/div[1]/span[2]/span[3]'
).text

# Extracting the duration from the timestamp
time_parts = duration_raw.split(':')

if len(time_parts) == 3:
    hours, minutes, seconds = map(int, time_parts)
elif len(time_parts) == 2:
    hours = 0
    minutes, seconds = map(int, time_parts)
else:
    input("Invalid video duration. Press enter to quit")
    exit(1)

duration = (hours * 3600) + (minutes * 60) + seconds

print(f"Found duration in seconds: {duration}\nStarting viewbot...")

for i in range(int(count)):
    driver.get(url)
    current_interval = get_interval()
    time.sleep(duration + current_interval)
    print("View sent")
    amount += 1
    os.system(f"title Youtube View Bot ^| Views Sent: {amount}")

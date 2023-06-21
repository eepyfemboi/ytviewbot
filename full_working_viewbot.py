import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Perflogs\chromedriver.exe"
amount = 0
os.system(f"title Youtube View Bot ^| Views Sent: {amount}")

video_list = []

# A function to collect a list of videos
def get_video_list():
    global video_list
    while True:
        url = input("Enter Video URL (say 'DONE' to continue): ")
        if url.lower() == "done":
            break
        video_list.append(url)

# Defining a function to always get a random number as the interval
def get_interval(time_1, time_2):
    return random.randrange(int(time_1), int(time_2))

def watch_video(url, driver: webdriver.Chrome):
    global amount

    # Getting the page initially
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
        input("Invalid video duration. Press enter to skip video")
        return

    duration = (hours * 3600) + (minutes * 60) + seconds

    print(f"Found duration in seconds: {duration}\nWatching video...")

    # Getting the current interval randomly
    current_interval = get_interval()

    # Waiting for the video to finish
    time.sleep(duration + current_interval)
    print("View sent")

    # Incrementing the amount
    amount += 1
    os.system(f"title Youtube View Bot ^| Views Sent: {amount}")

def __main__():
    # Sending a little welcome message
    print("Thanks for using my ViewBot! I recommend adding a few videos that aren't your own videos to the video list, to simulate a normal viewing session and keep YouTube from removing the views. Also, don't rely on this as your sole source of views. Get some real views bro. fr.")

    # Getting the video list
    get_video_list()

    # Getting the interval
    time_1 = input("Enter Minimum Time Between Views in seconds: ")
    time_2 = input("Enter Maximum Time Between Views in seconds: ")

    # Initializing the window
    driver = webdriver.Chrome(PATH)

    # Watching each video
    for url in video_list:
        watch_video(url, driver)
    
    # Closing the chrome page
    driver.close()
    
    # Finishing
    input(f"Finished watching {len(video_list)} videos. Press enter to quit...")

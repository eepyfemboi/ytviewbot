from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
from random import *

PATH = "C:\Perflogs\chromedriver.exe"

amount = 0
error = 0

os.system(f"title Youtube View Bot ^| Views Sent: {amount}^ | Error: {error}")

print("\n" * 80)

#views config
url = input("Enter Video URL: ")
count = input("Enter View Count: ")

#my temporary fix to not have to figure out the exact number of seconds long the video is
hour = input("Please input video length in hours. If this does not apply, please just enter 0: ")
minute = input("Please input video length in minutes. If this does not apply, please just enter 0: ")
second = input("Please input video length in seconds: ")

convminute = (int(hour)*60)+int(minute)
convsecond = (int(convminute)*60)+int(second)

#interval config
time1 = input("Enter Minimum Time Between Views in seconds: ")
time2 = input("Enter Maximum Time Between Views in seconds: ")

interval = randrange(int(time1), int(time2))

driver = webdriver.Chrome(PATH)


while (count == count):
  time.sleep(3)
  print(f"{Fore.GREEN} [-] Error")
  error += 1
  os.system(f"title Youtube View Bot ^| Views Sent: {amount}^| Error: {error}")
  driver.get(url)
  time.sleep(int(convsecond)+interval)
  print(f"{Fore.GREEN} [+] View")
  amount += 1
  os.system(f"title Youtube View Bot ^| Views Sent: {amount}^| Error: {error}")

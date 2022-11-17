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
#EXCET#4508

amount = 0
error = 0

os.system(f"title Youtube View Bot ^| Views Sent: {amount}^ | Error: {error}")

print("\n" * 80)

url = input("Enter Video URL: ")
count = input("Enter View Count: ")

time1 = input("Enter Minimum Time Between Views in seconds: ")
time2 = input("Enter Maximum Time Between Views in seconds: ")

interval = randrange((time1), (time2))

driver = webdriver.Chrome(PATH)


while (count == count):
  time.sleep(3)
  print(f"{Fore.GREEN} [-] Error")
  error += 1
  os.system(f"title Youtube View Bot ^| Views Sent: {amount}^| Error: {error}")
  driver.get(url)
  time.sleep(interval)
  print(f"{Fore.GREEN} [+] View")
  amount += 1
  os.system(f"title Youtube View Bot ^| Views Sent: {amount}^| Error: {error}")

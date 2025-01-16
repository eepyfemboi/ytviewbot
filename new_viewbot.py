import os
import sys
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import argparse


class ViewBot:
    def __init__(self):
        self.args: argparse.Namespace = ...
        self.url: str = ...
        self.views: int = ...
        self.minimum_view_interval: int = ...
        self.maximum_view_interval: int = ...
        self.chromedriver_path: str = ...
        self.views_done: int = ...
        self.driver: webdriver.Chrome = ...
        self.video_duration: int = ...
        self.bot_loop()

    def parse_cmd_args(self) -> None:
        parser = argparse.ArgumentParser()

        parser.add_argument("-u", "--url", help="the url of the youtube video to bot views on", type=str, default="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        parser.add_argument("-v", "--views", help="the amount of views to bot", type=int, default=25)
        parser.add_argument("-t", "--mintime", help="the minimum time between views in seconds", type=int, default=5)
        parser.add_argument("-T", "--maxtime", help="the maximum time between views in seconds", type=int, default=15)
        parser.add_argument("--chromepath", help="the path to the chromedriver.exe executable", type=str, default=os.path.expandvars("%USERPROFILE%\\chromedriver.exe"))

        self.args = parser.parse_args()
        
        self.url = self.args.url
        self.views = self.args.views
        self.minimum_view_interval = self.args.mintime
        self.maximum_view_interval = self.args.maxtime
        self.chromedriver_path = self.args.chromepath

    def update_title(self) -> None:
        os.system(f"title Youtube View Bot ^| Views Sent: {self.views_done}")
        print(f"Views Sent: {self.views_done}\n")

    def get_random_delay(self) -> int:
        return random.randrange(self.minimum_view_interval, self.maximum_view_interval)

    def get_video_duration(self) -> None: 
        self.driver.get(self.url)
        time.sleep(5)
        
        duration_raw: str = self.driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[33]/div[2]/div[1]/div[1]/span[2]/span[3]").text
        
        time_parts: list[str] = duration_raw.split(":")
        parts: int = len(time_parts)
        
        if (parts > 3) or (parts < 2):
            input("Something went wrong while fetching the video duration. Make an issue at https://github.com/eepyfemboi/ytviewbot to report this ig. Press `enter` to exit the script")
            sys.exit(1)
        elif parts == 3:
            hours, minutes, seconds = map(int, time_parts)
        elif parts == 2:
            hours = 0
            minutes, seconds = map(int, time_parts)

        self.video_duration = (hours * 3600) + (minutes * 60) + seconds

    def wait_for_video(self):
        time.sleep(self.video_duration + self.get_random_delay())

    def run_bot_view(self):
        self.driver.get(self.url)
        self.wait_for_video()
        self.views_done += 1
        self.update_title()

    def bot_loop(self):
        for i in range(self.views):
            self.run_bot_view()

    def initialize(self):
        self.parse_cmd_args()
        self.driver = webdriver.Chrome(self.chromedriver_path)
        self.get_video_duration()
        self.bot_loop()

if __name__ == "__main__:
    ViewBot()

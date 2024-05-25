"""
Program: toriyChek v1.3.5
Author: Richard Ortiz
Updated: 05.25.24
"""

# Define variables and import modules
import keyboard
import time
import os
import ctypes
import datetime


brave = \
    'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
siteList = [
    'torrentleech.org',
    'iptorrents.com',
    'filelist.io',
    'cinemaZ.to',
    'avistaZ.to',
    'exoticaZ.to',
    'animetorrents.me',
    'myanonamouse.net',
    'audionews.org'
    ]
counter = 0
now = datetime.datetime.now()

# Launch Brave after making sure it's closed
os.system('taskkill /f /im brave.exe')
os.startfile(brave)
time.sleep(1)

# For loop to launch sites sequentially, close browser and kill process, then display confirmation pop-up
for _ in siteList:
    time.sleep(0.5)
    keyboard.write(siteList[counter])
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+t')
    counter += 1
    time.sleep(0.5)
    if counter == 9:
        time.sleep(3)
        os.system('taskkill /f /im brave.exe')
        ctypes.windll.user32.MessageBoxW(0, "Checks have been completed at " + now.strftime("%H:%M") + "!", "Success", 0)
 
 
"""
backup siteList = [
    'torrentleech.org',
    'iptorrents.com',
    'filelist.io',
    'cinemaZ.to',
    'avistaZ.to',
    'exoticaZ.to',
    'animetorrents.me',
    'myanonamouse.net',
    'audionews.org'
    ]
    
fake siteList = [
    'torlami',
    'iptom',
    'fileliso',
    'cinemaZ',
    'avistaZ',
    'exoticaZ',
    'animetos',
    'amouse',
    'dionews'
    ]
"""
"""
Program: toriyChek v1.34
Author: Richard Ortiz
Updated: 05.09.24
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
    time.sleep(1)
    keyboard.write(siteList[counter])
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.press_and_release('f6')
    counter += 1
    time.sleep(1)
    if counter == 9:
        os.system('taskkill /f /im brave.exe')
        ctypes.windll.user32.MessageBoxW(0, "Authentication has been completed at " + now.strftime("%H:%M") + "!", "Success", 0)
 
 
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
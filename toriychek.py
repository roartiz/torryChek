"""
Program: toriyChek v1.33
Author: Richard Ortiz
Updated: 05.03.24
"""

# Define variables and import modules
import keyboard
import time
import os

brave = \
    'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
siteList = [
    'torrentleech.org',
    'iptorrents.com',
    'avistaZ.to',
    'cinemaZ.to',
    'exoticaZ.to',
    'animetorrents.me',
    'myanonamouse.net',
    'audionews.org',
    'filelist.io'
    ]
counter = 0

# Launch Brave after making sure it's closed
os.system('taskkill /f /im brave.exe')
os.startfile(brave)
time.sleep(1)

# For loop to launch websites sequentially, then close browser and kill process once done
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
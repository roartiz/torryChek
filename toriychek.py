# Program: toriyChek v1.31
# Author: Richard Ortiz
# Updated: 04.28.24

# Define variables and import modules
brave = \
    'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
siteList = [
    'torlami',
    'iptom',
    'filliso',
    'cimaZ',
    'astaZ',
    'eicaZ',
    'aniimetos',
    'amommamouse',
    'dionews'
    ]
counter = 0
import keyboard
import time
import os

# Launch Brave after making sure it's closed
os.system('taskkill /f /im brave.exe')
os.startfile(brave)
time.sleep(1)

# While loop to launch websites sequentially, then close browser and kill process once done (DISABLED SEND URL for test)
for _ in siteList:
    time.sleep(1)
    keyboard.write(siteList[counter])
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('f6')
    counter += 1
    if counter == 9:
        time.sleep(1)
        os.system('taskkill /f /im brave.exe')
 
"""
# backup siteList = [
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
# backup fake siteList = [
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
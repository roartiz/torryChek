# Program: toriyChek v1.2
# Author: Richard Ortiz
# Updated: 04.19.24

# Define variables and import modules
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
import keyboard
import time
import os

# Launch Brave after making sure it's closed
os.system('taskkill /f /im brave.exe')
os.startfile(brave)
time.sleep(1)

# While loop to launch websites sequentially
while counter < 9:
    time.sleep(1)
    keyboard.write(siteList[counter])
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('f6')
    counter += 1

# Close browser and kill process once done
if counter == 9:
    time.sleep(1)
    os.system('taskkill /f /im brave.exe')
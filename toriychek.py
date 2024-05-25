"""
Program: toriyChek v1.4.0
Author: Richard Ortiz
Updated: 05.25.24
"""

# Define variables and import modules
import keyboard
import time
import ctypes
import datetime
import subprocess

bravePath = \
    'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
text_file = open("siteList.txt", "r")
siteList = [line.strip() for line in text_file.readlines()]
text_file.close()


def closeBrave():
    # Kill Brave browser process
    try:
        subprocess.run(['taskkill', '/f', '/im', 'brave.exe'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Brave is closed!")
        
        
def openBrave():
    # Launch Brave browser
    try:
        subprocess.Popen(bravePath)
        time.sleep(1)
    except Exception as e:
        print(f"Failed to open Brave: {e}")


def openSites():
    # For loop to launch each site in a new tab, then let them all load
    for site in siteList:
        keyboard.write(site)
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+t')
        time.sleep(0.1)
    time.sleep(3)
    

def main():
    # Main function to control the process
    closeBrave()
    openBrave()
    openSites()
    closeBrave()

    # Display confirmation message
    now = datetime.datetime.now()
    completion_time = now.strftime("%H:%M")
    ctypes.windll.user32.MessageBoxW(0, f"Checks have been completed at {completion_time}!", "Success", 0)
    
    
if __name__ == "__main__":
    main()
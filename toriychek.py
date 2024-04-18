#Program: toriyChek v1.1
#Author: Richard Ortiz
#Updated: 04.13.24


# Define variables and import modules
brave = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe'
siteList = ["torrentleech.org", "iptorrents.com", "filelist.io", "cinemaZ.to", "avistaZ.to", "exoticaZ.to", "animetorrents.me", "myanonamouse.net", "audionews.org"]
index = 0
counter = int(index) #convert string to integer
import keyboard, time, os

# Launch browser and wait
os.startfile(brave)
time.sleep(1)

# For loop to launch websites sequentially (but opens one too many blank tabs still)
for index in siteList:
    time.sleep(1)
    keyboard.write(siteList[counter])
    keyboard.press_and_release('enter')
    counter += 1
    keyboard.press_and_release('ctrl+t')
    time.sleep(1)
    
# Close browser once done
if counter >= 9:
    time.sleep(2)
    keyboard.press_and_release('alt+f4')

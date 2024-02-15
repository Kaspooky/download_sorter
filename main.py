import os
import shutil
DesktopPath = 'C:\\Users\\Kacper\\Desktop'
downloadPath = 'C:\\Users\\Kacper\\Downloads'

file = open("moveLog.txt", "a")
for entries in os.listdir(r'C:\Users\Kacper\Downloads'):
    splitEntry = entries.split(".")
    if (splitEntry[-1] == "txt"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + splitEntry[-1])
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + splitEntry[-1] + "\n")
file.close()

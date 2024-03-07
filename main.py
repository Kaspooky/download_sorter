import os
import shutil
from datetime import datetime
DesktopPath = 'C:\\Users\\Kacper\\Desktop'
downloadPath = 'C:\\Users\\Kacper\\Downloads'
file = open("moveLog.txt", "a")
today = datetime.today().strftime('%m/%d/%Y')
time = datetime.today().strftime('%H:%M:%S')
for entries in os.listdir(r'C:\Users\Kacper\Downloads'):
    splitEntry = entries.split(".")
    ext = splitEntry[-1]
    if not os.path.isdir(DesktopPath + "\\" + ext):
        os.makedirs(DesktopPath + "\\" + ext)
    else:
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + ext)
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + ext + " on " + today + " at " + time + "\n")
file.write("File sorting has finished at: " + time + " on " + today + ".")
file.close()

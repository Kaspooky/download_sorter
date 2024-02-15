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
    # Sort all 'txt' or 'docx' files into 'txt' folder located on desktop
    if (splitEntry[-1] == "txt" or splitEntry[-1] == "docx"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "txt")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "txt" + " on " + today + " at " + time + "\n")
    # Sort all PDF file types into 'pdfs' folder located on desktop
    elif (splitEntry[-1] == "pdf"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "pdfs")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "pdfs" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "mov" or splitEntry[-1] == "mp4"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "videos")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "videos" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "zip" or splitEntry[-1] == "tar" or splitEntry[-1] == "7z" or splitEntry[-1] == "rar" or splitEntry[-1] == "gz"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "zip")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "zip" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "png" or splitEntry[-1] == "jpeg" or splitEntry[-1] == "jpg" or splitEntry[-1] == "gif"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "images")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "images" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "exe"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "applications")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "applications" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "msi"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "installers")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "installers" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "xlsx" or splitEntry[-1] == "pptx"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "msuite")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "msuite" + " on " + today + " at " + time + "\n")
    elif (splitEntry[-1] == "mp3"):
        shutil.move(downloadPath + '\\' + entries,
                    DesktopPath + '\\' + "music or sounds")
        file.write("file: " + entries + " from: " + downloadPath +
                   " --> " + DesktopPath + '\\' + "music or sounds" + " on " + today + " at " + time + "\n")
file.close()

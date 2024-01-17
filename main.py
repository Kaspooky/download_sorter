import os
file = open("testfile", "w")
for entries in os.listdir(r'C:\Users\Kacper\Downloads'):
    splitEntry = entries.split(".")
    if (splitEntry[-1] == "txt"):
        file.write(entries + "\n")
file.close()

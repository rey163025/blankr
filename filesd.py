import datetime
import os

def file_info():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    for file in os.listdir(desktop):
        print(f"Name: {file} # Path: {os.path.join(desktop, file)} # Size: {os.path.getsize(os.path.join(desktop, file))} bytes \
# Creation date: {datetime.date.fromtimestamp(os.path.getctime(os.path.join(desktop,file)))}")


file_info()
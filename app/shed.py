from Tkinter import *
import tkMessageBox
import schedule
import time

def job():
    tkMessageBox.showinfo("Test", "Good job")


schedule.every(.1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
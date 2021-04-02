from tkinter import *
from tkinter.ttk import *
from queue import Queue

class OverallProgressBar:

    def __init__(self, q: Queue):
        root = Tk()
        root.title("Progress")
        root.geometry("+300+200")

        Label(root, text=f"Overall Progress:").pack()
        self.progress = Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress.pack()
        self.progressLabel = Label(root, text="0%")
        self.progressLabel.pack()
        while True:
            percent = int(q.get())
            self.progress["value"] = percent
            self.progress.update()
            self.progressLabel.config(text=f"{percent}%")
            q.task_done()
            root.update()
            if percent >= 100:
                break
        root.destroy()

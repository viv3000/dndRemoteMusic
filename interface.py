import threading

from tkinter import ttk, Tk, Label
from tkthread import tk, TkThread


from helpers import *


class Interface():
    pass


class InterfaceCli(Interface):
    def __init__(self, settings=Settings()):
        super().__init__()
        self.settings = settings


    def run(self):
        while self.settings.isRun:
            for i in self.settings.musicFiles:
                print(i)
            self.settings.selectedMusicFile = self.settings.musicFiles[int(input("input number: "))]


class MusicButton(ttk.Button):
    def __init__(self, musicFile, settings, master=None, **kw):
        def event():
            settings.selectedMusicFile = musicFile

        super().__init__(master, text=musicFile, command=event, **kw)


class DndMusicForm(Interface):
    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self.root: Tk = Tk()
        self.settings = settings
        self.size = [900, 500]
        self.musicButtonSize = [100, 50]
        self.musicButtonGaps = [30, 30]

        self.createMusicPanel(self.root)

    def createMusicPanel(self, master):
        musicFiles = getMusicFiles()
        frameMenu = ttk.Frame(master)
        frameMenu.pack()
        frame = ttk.Frame(master)
        frame.pack()

        def exit(): 
            self.settings.isRun = False
            self.root.destroy()

        ttk.Button(frameMenu, text="X", command=exit).pack()

        for i in range(len(musicFiles)):
            MusicButton(musicFiles[i], self.settings, frame).pack()

    def start(self):
        self.root.mainloop()


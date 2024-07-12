import asyncio
import glob
import os
import multiprocessing
import time
import sys, traceback

from settings import *


class Log:
    def __init__(self):
        pass

    def info(self, text: str):
        print(text)

    def error(self, ex: Exception=None, message:str=None):
        if (message!=None):
            print(message)
        if (ex != None):
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)


class Player:
    def __init__(self, settings):
        self.settings = settings
        self.file = None
        self.playProcess = None

    def setPlayProcess(self, newPlayProcess):
        self.playProcess = newPlayProcess

    def run(self):
        try:
            if (os.name == 'posix'):
                import subprocess
                self.setPlayProcess(subprocess.Popen(["ffplay", "-nodisp", f"{self.file}"], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT))
            else:
                from playsound import playsound
                self.playProcess = multiprocessing.Process(target=playsound, args=(self.file,))
            print(f"playFile {self.file}")
        except Exception as ex:
            Log().error(ex, "in play")

    def stop(self):
        self.playProcess.terminate()

    async def changeFile(self, file):
        self.file = file


class PlayerThread(multiprocessing.Process):
    def __init__(self, settings, player):
        super().__init__()
        self.player = player
        self.settings = settings

    def start(self):
        self.player.run()

    def terminate(self):
        self.player.stop()
        super().terminate()

def calculatePointForPeriodWidget():
    pass

def getMusicFiles():
    return glob.glob("musics/*.mp3")



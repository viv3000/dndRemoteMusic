from settings import *

class SettingsClient(Settings):
    def __init__(self):
        self.musicFiles = ["musics/GoodBadEvil.mp3", "musics/LeEventLeCri.mp3"]
        self.selectedMusicFile = self.musicFiles[0]
        self.isRun = True
        self.port = 32781
        self.ip = 'tcp://tcp-free.tunnel4.com'
        self.timeout = 2

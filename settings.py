class Settings:
    def __init__(self):
        self.musicFiles = ["musics/GoodBadEvil.mp3", "musics/LeEventLeCri.mp3"]
        self.selectedMusicFile = self.musicFiles[0]
        self.isRun = True
        self.port = 9090
        self.ip = '127.0.0.1'
        self.timeout = 2

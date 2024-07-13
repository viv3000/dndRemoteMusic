import socket
import time
import asyncio
import pdb

from helpers import Log, Player, Settings, PlayerThread
from settings import *

clients = {}  # task -> (reader, writer)

log = Log()

class AsyncClient:
    def __init__(self,  settings: Settings, player: Player):
        self.settings = settings
        self.player: Player = player
        self.playerThread: PlayerThread = None
    
    async def getMusic(self, reader, writer):
        try:
            message = "getMusicFile"
            writer.write(message.encode())
            await writer.drain()
            data = await reader.read(100)
            musicFile = data.decode()
            if (self.player.file != musicFile):
                if (self.playerThread != None):
                    self.playerThread.player.stop()
                self.playerThread = PlayerThread(self.settings, self.player)
                self.player.file = musicFile
                self.playerThread.start()
            else:
                self.player.file = musicFile
        except Exception as ex:
            log.error(ex, "in getMusic")

    async def runLoop(self):
        writer = None
        try:
            log.info("start client")
            reader, writer = await asyncio.open_connection(self.settings.ip, self.settings.port)
        
            while True:
                time.sleep(3)
                await self.getMusic(reader, writer)
        except Exception as ex:
            log.error(ex, "in main loop")
        finally:
            if (writer != None):
                log.info('Close the connection')
                writer.close()
                await writer.wait_closed()

async def main():
    settings = Settings()
    player = Player(settings)
    client = AsyncClient(settings, player)

    clientTask = asyncio.create_task(client.runLoop())
    
    await clientTask

asyncio.run(main())


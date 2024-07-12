import asyncio
import threading

from helpers import Log, Settings
from interface import *
from settings import *

log = Log()

class AsyncServer:
    def __init__(self, settings: Settings):
        self.settings = settings

    async def loop(self, reader, writer):
        while self.settings.isRun:
            try:
                data = await reader.read(100)
                message = data.decode()
                addr = writer.get_extra_info('peername')
                log.info(f"Received {message!r} from {addr!r}")
                
                send = self.settings.selectedMusicFile
                log.info(f"Send: {send!r}")
                writer.write(bytes(send, encoding='UTF-8'))
                await writer.drain()
            except Exception as ex:
                log.error(ex, "in handle")
                break
        log.info("Close the connection")
        writer.close()

    async def runLoop(self):
            server = await asyncio.start_server(
                self.loop, self.settings.ip, self.settings.port)

            addr = server.sockets[0].getsockname()
            log.info(f'Serving on {addr}')

            async with server:
                await server.serve_forever()


def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def main():
    settings = Settings()
    server = AsyncServer(settings)

    loop = asyncio.new_event_loop()
    threading.Thread(target=start_background_loop, args=(loop, )).start()
    asyncio.run_coroutine_threadsafe(server.runLoop(), loop)

    DndMusicForm(settings).start()


if __name__ == "__main__":
    asyncio.run(main())

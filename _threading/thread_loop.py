from threading import Thread
from time import sleep


class ThreadLoop(Thread):

    def __init__(self, loop, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.running = False
        self.__loop = loop

    def start(self) -> None:
        self.running = True
        super().start()

    def run(self) -> None:
        while self.running:
            self.__loop()
            sleep(0.1)

    def stop(self):
        self.running = False

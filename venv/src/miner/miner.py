from abc import ABC, abstractclassmethod


class Miner(ABC):
    @abstractclassmethod
    def runminer(self):
        pass


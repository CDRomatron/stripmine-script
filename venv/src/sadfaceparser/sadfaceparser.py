from abc import ABC, abstractclassmethod


class Sadfaceparser(ABC):
    @abstractclassmethod
    def tosadface(self):
        pass
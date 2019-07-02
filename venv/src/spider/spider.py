from abc import ABC, abstractclassmethod


class Spider(ABC):
    @abstractclassmethod
    def runspider(self):
        pass


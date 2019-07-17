from abc import ABC, abstractclassmethod

#The spider class forms the basis of how the text that is to be mined is gathered

#The return of runspider should return an array of Spiderextract objects

class Spider(ABC):
    @abstractclassmethod
    def runspider(self):
        pass


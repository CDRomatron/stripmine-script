from abc import ABC, abstractclassmethod


class Database(ABC):
    @abstractclassmethod
    def insertvalue(self):
        pass

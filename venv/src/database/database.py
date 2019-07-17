from abc import ABC, abstractclassmethod

#The Database class exists to write the produced SADFace json documents into a database

#The Database class should accept SADFace json documents

class Database(ABC):
    @abstractclassmethod
    def insertvalue(self):
        pass

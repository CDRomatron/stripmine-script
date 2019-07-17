from abc import ABC, abstractclassmethod

#The miner class contains the method used for identifying arguments in text

#The miner class should accept the text from a Spiderextract object

#The miner class should output a json object
#A matching Sadfaceparser class should be written to interprate the json into the SADFace format

class Miner(ABC):
    @abstractclassmethod
    def runminer(self):
        pass


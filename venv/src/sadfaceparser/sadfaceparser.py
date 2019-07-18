from abc import ABC, abstractclassmethod

#The Sadfaceparser class converts the json recieved by the miner into the standard SADFace format
#When a new miner is used, a new parser will need to be build to interperate the json

#The Sadfaceparser class should accept a json

#The Sadfaceparser class should output a SADFace json

#for additional metadata to be displayed on the sadface webapp, use ['metadata']['extended']

class Sadfaceparser(ABC):
    @abstractclassmethod
    def tosadface(self):
        pass
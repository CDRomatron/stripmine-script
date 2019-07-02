from miner.miner import Miner
import subprocess
import os


def savetext(text, dir):
    f = open(os.getcwd() + dir + 'temp.txt', 'w+')
    f.write(text)
    f.close

class Margotminer(Miner):
    directory = ''

    def __init__(self, dir):
        self.directory = dir


    def runminer(self, text, id):
        savetext(text, self.directory)
        subprocess.call("./run_margot.sh temp.txt output_" + id, shell=True, cwd=os.getcwd() + self.directory)

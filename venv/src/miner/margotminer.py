from miner.miner import Miner
import subprocess
import os
import json


def savetext(text, dir):
    f = open(os.getcwd() + dir + 'temp.txt', 'w+')
    f.write(text)
    f.close

def openfile(dir, id):
    with open(os.getcwd() + dir + 'output_' + id + '/OUTPUT.json') as f:
        return json.load(f)

class Margotminer(Miner):
    directory = ''

    def __init__(self, dir):
        self.directory = dir


    def runminer(self, text, id):
        savetext(text, self.directory)
        subprocess.call("./run_margot.sh temp.txt output_" + id, shell=True, cwd=os.getcwd() + self.directory)
        return openfile(self.directory, id)

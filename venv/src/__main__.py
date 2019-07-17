from spider.redditspider import RedditSpider
from miner.margotminer import Margotminer
from sadfaceparser.margotsadfaceparser import Margotsadfaceparser
from database.mongodatabase import Mongodatabase
import json


configfile = 'config.json'

with open(configfile) as f:
    config = json.load(f)
f.close()


spider = RedditSpider(config['reddit'])
miner = Margotminer('/miner/predictor/')
parser = Margotsadfaceparser('/miner/predictor/')
database = Mongodatabase(config['database'])

data = spider.runspider()
print("spider finished!")
count = 0
for item in data:
    jsonout = miner.runminer(item.text, str(count))
    print("miner done! " + str(count))
    sadfaceout = parser.tosadface(jsonout, item.meta)
    database.insertvalue(sadfaceout)
    print("database inserted! "+str(count))
    count += 1



print("done!")
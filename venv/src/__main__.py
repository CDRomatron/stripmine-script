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
miner.runminer(spider.runspider()[0], '0')

parser = Margotsadfaceparser('/miner/predictor/')

database = Mongodatabase(config['database'])
database.insertvalue(parser.tosadface('0'))

print("done!")
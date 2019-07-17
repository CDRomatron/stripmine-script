from spider.spider import Spider
import praw
from spiderextract import Spiderextract


def getNew(reddit, sub, n):
    submissions = []
    for submission in reddit.subreddit(sub).new(limit=n):
        meta = {}
        meta['Title'] = submission.title
        meta['Author'] = submission.author.name
        meta['Source'] = 'https://reddit.com' + submission.permalink
        meta['Fulltext'] = submission.selftext
        submissions.append(Spiderextract(submission.selftext, meta))
    return submissions


class RedditSpider(Spider):
    redditinstance = None

    def __init__(self, auth):
        self.redditinstance = praw.Reddit(client_id=auth['cid'],
                         client_secret=auth['cse'],
                         user_agent=auth['uag'])


    def runspider(self):
        return getNew(self.redditinstance, 'changemyview', 1)


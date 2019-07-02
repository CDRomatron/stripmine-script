from spider.spider import Spider
import praw


def getNew(reddit, sub, n):
    submissions = []
    for submission in reddit.subreddit(sub).new(limit=n):
        submissions.append(submission.selftext)
        print(submission.selftext)
    return submissions


class RedditSpider(Spider):
    redditinstance = None

    def __init__(self, auth):
        self.redditinstance = praw.Reddit(client_id=auth['cid'],
                         client_secret=auth['cse'],
                         user_agent=auth['uag'])


    def runspider(self):
        return getNew(self.redditinstance, 'changemyview', 1)


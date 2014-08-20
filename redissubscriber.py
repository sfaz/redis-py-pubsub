from threading import Thread
import redis
import json
from collections import Counter

'''
This application is run standalone to subscribe to the events sent out by redis
'''

stats = Counter()

class Listener(Thread):
    def __init__(self, r, channels):
        Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
    
    def work(self, item):
        try:
            mydata = json.loads(item['data'])
            stats[mydata['option']] += 1
            print stats
        except:
            print "Error" + item['channel'], ":", item['data']
    
    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print self, "unsubscribed and finished"
                break
            else:
                self.work(item)
                
r = redis.Redis()
client = Listener(r, ['test'])
client.start()
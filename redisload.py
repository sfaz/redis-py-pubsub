import redis
import time
import uuid
import requests
from threading import Thread
import random
import json
from datetime import datetime

MAX = 10000
r = redis.StrictRedis(host='localhost', port=6379, db=0)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

vote_options = ['A','B','C','D','E']
request_count = 0
request_errors = 0

def make_request():
    global request_count
    global request_errors
    for i in range(0, 200):
        try:
            data = {'poll':'testpoll','option':random.choice(vote_options)}
            resp = requests.post("http://localhost:6223/create",data=data)
            if resp.status_code == 200:
                request_count += 1
        except:
            print "Error"
            request_errors += 1
        
start = time.time()
ts = []
#print time.strftime("%H:%M:%S", start)
for i in range(0, 100):
    print i, time.strftime("%H:%M:%S", time.localtime())
    t = Thread(target=make_request)
    t.start()
    ts.append(t)


#print time.strftime("%H:%M:%S", finish)
for t in ts:
    t.join()
FMT = '%H:%M:%S'
finish = time.time()
tdelta = finish - start
print "Requests: " + str(request_count)
print "TPS: %s" % (request_count/tdelta)
print request_errors

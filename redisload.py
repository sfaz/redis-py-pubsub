import redis
import time
import uuid
import requests
from threading import Thread
import random
import json

MAX = 100000
r = redis.StrictRedis(host='localhost', port=6379, db=0)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

vote_options = ['A','B','C','D','E']

def make_request():
    for i in range(0, 100):
        data = {'poll':'testpoll','option':random.choice(vote_options)}
        requests.post("http://localhost:6223/create",data=data)
        
start = time.localtime()
print time.strftime("%H:%M:%S", start)
for i in range(0, MAX/100):
    t = Thread(target=make_request())
    t.start()

finish = time.localtime()
print time.strftime("%H:%M:%S", finish)
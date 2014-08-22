redis-py-pubsub
===============

A small test of high volume redis based pub sub or incremental value storage. Testing on a Macbook Pro (i7) achieved a TPS of ~500 posts per second with this.

The initial test case for this is a high volume polling solution where usings would simply vote for a value e.g. A,B,C,D,E etc and the values can either be summed directly in redis using the incr command or by using the subscriber function which then sums up the values in a Python Counter dict.

To set this up there are 3 main components:
1. redisserver.py - this is a Flask app run in the tornado wsgi applicaiton, it simply takes post commands sent to http//server/create and stores these either as a counter or does a store to redis and pushes them out to a subscriber as a transaction
2. redisload.py - this is a simple application that simply generates some random
3. redisubcriber.py - this is the subscriber to the redis publish commands if that option is used

Note to get all the components run:
    pip install -r requirements.txt
    

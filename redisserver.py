from flask import Flask, request
import uuid
import redis
import json

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/create', methods=['GET','POST'])
def create():
    data = json.dumps(request.form)
    pipe = r.pipeline()
    key = uuid.uuid4()
    #r.incr(request.form['option'])
    pipe.publish('test', data)
    pipe.set(key, data)
    pipe.execute()
    return "OK"

if __name__ == "__main__":
    # add the handlers to the console for local debug
    app.debug = True
    app.run(host="0.0.0.0", port=6222)
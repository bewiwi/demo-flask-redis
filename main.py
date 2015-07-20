import platform

from flask import Flask
from flask_redis import Redis

app = Flask(__name__)
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_DB'] = '5'

redis = Redis(app)


@app.route('/')
def homepage():
    count = int(redis.get('count'))
    if not count:
        count = 0
    redis.set('count', count + 1)
    return "Hi, I'm %s, this page has been seen %d times." % (
        platform.node(), count)


if __name__ == "__main__":
    app.run(debug=True)

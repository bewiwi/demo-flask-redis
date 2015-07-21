import platform
import codecs
import yaml

from flask import Flask
from flask_redis import Redis

app = Flask(__name__)
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_DB'] = '5'
app.config['REDIS_KEY'] = 'count'


# Locate the config file to use
config_file = 'config.yml'
try:
    # Open and read the config file
    with codecs.open(config_file, 'r', 'utf8') as file_handler:
        conf = yaml.load(file_handler)
        app.config.update(conf)
except Exception as e:
    print 'Error: %s' % e
redis = Redis(app)


@app.route('/')
def homepage():
    count = redis.get(app.config['REDIS_KEY'])
    if not count:
        count = 1
    redis.set(app.config['REDIS_KEY'], int(count) + 1)
    return "Hi, I'm %s, this page has been seen %s times." % (
        platform.node(), count)


if __name__ == "__main__":
    app.run(debug=True)

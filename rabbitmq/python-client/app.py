from flask import Flask
app = Flask(__name__)

import datetime, logging, sys, json_logging, flask, pika

app = flask.Flask(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init(framework_name='flask')
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

@app.route("/greeting")
def greeting():

    credentials = pika.PlainCredentials('rabbitmq', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    return "Hello World!"
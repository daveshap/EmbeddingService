import flask
import logging
import json
from flask import request
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text  # Registers the ops.


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = flask.Flask('encoder')


@app.route('/', methods=['post'])
def home():
    payload = request.json  # payload should be like "asdfasdf"
    print(payload)
    embeddings = encoder(list(payload))
    result = str(embeddings[0].numpy().tolist()[0])
    #print(result)
    return flask.Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    hub_url = "https://tfhub.dev/google/universal-sentence-encoder-lite/2"
    encoder = hub.load(hub_url)
    #encoder = hub.KerasLayer(hub_url)
    app.run(host='0.0.0.0', port=999)
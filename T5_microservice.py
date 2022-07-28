import flask
import json
from flask import request
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text  # Registers the ops.


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
    #app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    #embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    hub_url = "https://tfhub.dev/google/sentence-t5/st5-base/1"
    encoder = hub.KerasLayer(hub_url)
    app.run(host='0.0.0.0', port=999)
import json
import os
from pprint import pprint
from deeppavlov import build_model, configs
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from bert_serving.client import BertClient
from flask_cors import CORS
from glob import glob

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origin': '*'}})

model = build_model(configs.squad.squad_bert, download=True)


def find_context(context_id):
    for f_name in glob('./topics/*.json'):
        name = os.path.basename(f_name)
        if context_id.split('_')[0] in name:
            with open(f_name, 'r') as f:
                data = json.load(f)
                for d in data.get('data'):
                    if d.get('id') == context_id:
                        return d.get('context')
    return ''


def create_query_vector(query):
    return BertClient().encode([query])[0]


def script_query(query_vector):
    return {
            "script_score": {
                "query": {
                    "match_all": {}
                },
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'text_vector') + 1.0",
                    "params": {
                        "query_vector": query_vector.tolist()
                    }
                }
            }
        }


def search(query):
    client = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return client.search(
        index="squad1.1",
        body={
                "size": 5,
                "query": query,
                # "_source": {"includes": ["context_id, question"]}
            }
    )


@app.route('/qna')
def qna():
    query = request.args.get('q')
    search_result = search(script_query(create_query_vector(query)))

    hit = (search_result.get("hits").get("hits"))[0]
    source = hit.get("_source")
    question = source.get("question")
    context_id = source.get("context_id")

    context = find_context(context_id)

    result = model([context], [question])
    response = {
                "context": context,
                "answer": result[0][0]
                }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

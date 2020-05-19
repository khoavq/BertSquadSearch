import json
import os
from pprint import pprint

import redis
from deeppavlov import build_model, configs
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from bert_serving.client import BertClient
from flask_cors import CORS
from glob import glob

app = Flask(__name__)
app.config.from_object(__name__)
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

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


def search(size, query):
    client = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return client.search(
        index="squad1.1",
        body={
            "size": size,
            "query": query,
            # "_source": {"includes": ["context_id, question"]}
        }
    )


@app.route('/qna')
def qna():
    query = request.args.get('q')
    pprint(f"USER INPUT QUESTION: {query}")
    size = request.args.get('limit')
    pprint(f"LIMIT SEARCH RESULT: {size}")
    search_result = search(size, script_query(create_query_vector(query)))

    answers = []
    hits = (search_result.get("hits").get("hits"))
    for hit in hits:
        score = hit.get("_score")
        source = hit.get("_source")
        question = source.get("question")
        context_id = source.get("context_id")
        context = find_context(context_id)
        # get answer from redis
        print(f"MATCHING QUESTION: {question}")
        if len(redis_db.hgetall(question)) != 0:
            pprint("FOUND ANSWER FROM CACHED")
            answer = {
                "score": redis_db.hget(question, "score").decode("utf-8"),
                "context": redis_db.hget(question, "context").decode("utf-8"),
                "question": redis_db.hget(question, "question").decode("utf-8"),
                "answer": redis_db.hget(question, "answer").decode("utf-8")
            }
        else:
            result = model([context], [question])
            ans = result[0][0]
            answer = {
                "score": score,
                "context": context,
                "question": question,
                "answer": ans
            }
            pprint(f"FOUND ANSWER: {ans}")
            # cache result having highest score = 2.0
            if score >= 2.0:
                redis_db.hset(question, "score", score)
                redis_db.hset(question, "context", context)
                redis_db.hset(question, "question", question)
                redis_db.hset(question, "answer", ans)
                pprint(f"CACHED RESULT")
        answers.append(answer)
    return jsonify(answers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

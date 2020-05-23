
import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def load_dataset(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def main():
    client = Elasticsearch()
    docs = load_dataset("squad_question_2.0.jsonl")
    bulk(client, docs)


if __name__ == '__main__':
    main()

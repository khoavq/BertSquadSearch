import json
from bert_serving.client import BertClient
from pprint import pprint

bc = BertClient(output_fmt='list', check_length=False)


def create_question_document(d_id, question, is_impossible, emb):
    return {
        '_op_type': 'index',
        '_index': 'squad2.0',
        'context_id': d_id,
        'question': question,
        'is_impossible': is_impossible,
        'text_vector': emb
    }


def main():
    f = open("./dataset/questions/all_questions.json", encoding="utf8")
    docs = json.load(f)
    questions = docs.get("data")
    with open("squad_question_2.0.jsonl", 'w') as f:
        for question in questions:
            print(question)
            q = question.get("question")
            is_impossible = question.get("is_impossible")
            d_id = question.get('id')
            a = create_question_document(d_id, q, is_impossible, bc.encode([q])[0])
            pprint(a)
            f.write(json.dumps(a) + '\n')


if __name__ == '__main__':
    main()

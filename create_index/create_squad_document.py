import json
from bert_serving.client import BertClient

bc = BertClient(output_fmt='list', check_length=False)


def create_question_document(d_id, question, emb):
    return {
        '_op_type': 'index',
        '_index': 'squad1.1',
        'context_ id': d_id,
        'question': question,
        'text_vector': emb
    }


def main():
    f = open("./dataset/questions/all_questions.json", encoding="utf8")
    docs = json.load(f)
    questions = docs.get("data")
    with open("squad_question.jsonl", 'w') as f:
        for question in questions:
            print(question)
            q = question.get("question")
            d_id = question.get('id')
            a = create_question_document(d_id, q, bc.encode([q])[0])
            f.write(json.dumps(a) + '\n')


if __name__ == '__main__':
    main()

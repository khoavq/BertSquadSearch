import json
from glob import glob
from pprint import pprint


def create_topics_files():
    file = open('./dataset/squad_dev-v2.0.json', encoding='utf8')
    data = json.load(file)
    for index, topic in enumerate(data.get('data')):
        title = topic.get('title')
        paragraphs = topic.get('paragraphs')
        context_list = []
        for i, paragraph in enumerate(paragraphs):
            questions_list = []
            for q in paragraph.get('qas'):
                question = {
                    'question': q.get('question'),
                    'is_impossible': q.get('is_impossible')
                }
                questions_list.append(question)
            content = {
                'id': f'{index + 1}_{i + 1}',
                'context': paragraph.get('context'),
                'questions': questions_list
            }
            context_list.append(content)
        data = {
            'data': context_list
        }

        with open(f'./dataset/topics/{index + 1}_{title}.json', 'w') as f:
            f.write(json.dumps(data) + '\n')


def create_all_questions_file():
    question_list = []
    for f_name in glob('./dataset/topics/*.json'):
        file = open(f_name, 'r')
        data = json.load(file)

        for d in data.get('data'):
            for question in d.get('questions'):
                content = {
                            'id': d.get('id'),
                            'question': question.get('question'),
                            'is_impossible': question.get('is_impossible')
                            }
                question_list.append(content)
    with open('./dataset/questions/all_questions.json', 'w') as f:
        ql = {
            'data': question_list
        }
        f.write(json.dumps(ql) + '\n')


def main():
    create_topics_files()
    create_all_questions_file()


if __name__ == '__main__':
    main()

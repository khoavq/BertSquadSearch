from elasticsearch import Elasticsearch


def main():
    index_name = 'squad2.0'
    print("Creating index")
    client = Elasticsearch()
    client.indices.delete(index=index_name, ignore=[404])
    with open("squad_questions_mapping.json") as index_file:
        source = index_file.read().strip()
        client.indices.create(index=index_name, body=source)
    print("Created!")


if __name__ == '__main__':
    main()

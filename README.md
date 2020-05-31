#### 1. Install python and virtual environment
* Install python
* Install pip
* Install virtualenv, and create venv environment

Activate virtual environment
In cmd or terminal, change directory to the root project folder, run `activate venv`

#### 2. bert-as-service server
Download BERT-Base, Cased from this [link](https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip)
Extract the zip file to your local folder, [your_desktop]/dev/cased_L-12_H-768_A-12/
Run `pip install -r /bertserving/requirements.txt`
Open the new terminal and change directory to the project root, active venv
Run: `bert-serving-start -model_dir=[your_desktop]/dev/cased_L-12_H-768_A-12/ -num_worker=4`

#### 3. Elasticsearch server
Follow this link to [download](https://www.elastic.co/downloads/elasticsearch) and run elasticsearch

Open the new terminal and change directory to the project root, active venv
Run `bin/elasticsearch` (or `bin\elasticsearch.bat` on Windows)
Run `curl http://localhost:9200/`(this command is to test if Elasticsearch is running)

#### 4. Index all questions
Open the new terminal and change directory to the project root, active venv
Change directory to create_index/
Run `pip3 install -r requirements.txt`
Run `python3 data_processing.py` to generate an all questions file and all topics files
Run `python3 create_quad_document.py` to create all questions index in json format
Run `python3 index_squad.py` to put the questions index to elasticsearch

#### 5. API
Open the new terminal and change directory to the project root, active venv
Run `pip3 install -r requirements.txt`
Run `pip3 install -r /venv/Lib/site-packages/deeppavlov/requirements/bert_dp.txt`
Run `python3 app.py`(it will take time to download bert models)

#### 6. Run web client
Open the new terminal and change directory to the project root, active venv
change directory to `client` folder
Run `npm install`
Run `npm start`


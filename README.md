Download or clone the source code to C:\dev (create dev folder if not exist)  
#### 1. Install python and virtual environment
* Download and install python [v3.7.7](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe)
* Open new Command Line (cmd), run the following commands:  
  install virtualenv `python -m pip install virtualenv`   
  change directory to the root project folder `cd C:\dev\BertSquadSearch`  
  create virtual environment, named venv `python -m venv venv`  
  active venv `.\venv\Scripts\activate`  

#### 2. bert-as-service server
Download BERT-Base, Cased from this [link](https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip)  
Extract the zip file to C:\dev\cased_L-12_H-768_A-12\  
Run `pip install -r C:\dev\bertserving\requirements.txt`  
Make sure you are still in venv (step 1)
Run `bert-serving-start -model_dir=C:\dev\cased_L-12_H-768_A-12/ -num_worker=2`  

#### 3. Elasticsearch server
Follow this link to [download Elasticsearch v7.7.1](https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.1-windows-x86_64.zip)  
Unzip to C:\dev\
Open new cmd, run `cd C:\dev\BertSquadSearch`, then `.\venv\Scripts\activate` 
Run `C:\dev\elasticsearch-7.7.1\bin\elasticsearch.bat`    
Run `curl http://localhost:9200/`(this command is to test if Elasticsearch is running)  

#### 4. Index all questions 
Open new cmd, run `cd C:\dev\BertSquadSearch`, then `.\venv\Scripts\activate` 
`cd C:\dev\BertSquadSearch\create_index\`  
`pip install -r requirements.txt` 
Create index `python create_squad_index.py`
You can unzip C:\dev\BertSquadSearch\create_index\squad_question_2.0.jsonl.zip to the same create_index folder  
And run `python index_squad.py` to put the questions index to elasticsearch  
OR  
Generate all questions file and all topics files `python3 data_processing.py`  
Create all questions index in json format  `python3 create_quad_document.py`   
Run `python3 index_squad.py` to put the questions index to elasticsearch

#### 5. API
Open new cmd, run `cd C:\dev\BertSquadSearch`, then `.\venv\Scripts\activate` 
`cd C:\dev\BertSquadSearch\api`
`pip install -r requirements.txt`  
`pip install -r C:\dev\BertSquadSearch\venv/Lib\site-packages\deeppavlov\requirements/bert_dp.txt`  
Download and install [redis](https://github.com/microsoftarchive/redis/releases/download/win-3.2.100/Redis-x64-3.2.100.msi)  
`python app.py`(it takes time to download models)  

#### 6. Run web client
Download and install [node.js](https://nodejs.org/dist/v12.18.0/node-v12.18.0-x64.msi)
`cd C:\dev\BertSquadSearch\client\`  
`npm install`  
`npm start`  
Open `localhost:3000` on your browser


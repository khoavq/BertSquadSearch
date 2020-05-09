Install python
Install pip
Install virtualenv
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

activate venv





Run bert-as-service server

pip install -r /bertserving/requirements.txt

Download BERT-Base, Cased from this link https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip
Extract the zip file to your local folder, [your_desktop]/dev/cased_L-12_H-768_A-12/
Open the new terminal and change directory to the project root, activate venv
Then run: bert-serving-start -model_dir=[your_desktop]/dev/cased_L-12_H-768_A-12/ -num_worker=4





Run Elasticsearch server

Follow this link to download and run elasticsearch https://www.elastic.co/downloads/elasticsearch

Download and unzip Elasticsearch
Run bin/elasticsearch (or bin\elasticsearch.bat on Windows)
Run curl http://localhost:9200/ or Invoke-RestMethod http://localhost:9200 with PowerShell 
(this command to test if Elasticsearch is running)

Index all questions
open new terminal (or new tab)
active venv: source /venv/bin/activate (Mac OS)
change directory to create_index/
run pip3 install -r requirements.txt

run python3 data_processing.py to generate an all questions file and all topics files
run python3 create_quad_document.py to create all questions index in json format
run python3 index_squad.py to put the questions index to elasticsearch




Run API
open new terminal (or new tab)
active venv: source /venv/bin/activate (Mac OS)
run pip3 install -r requirements.txt
run pip3 install -r /venv/Lib/site-packages/deeppavlov/requirements/bert_dp.txt
run python3 app.py
(it will take time to download bert models)



Run web client
open new terminal (or new tab)
change directory to client
run npm install
run npm start


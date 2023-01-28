<img src=".github/saymysearch.png">


<p align="center">
<em>A small search engine based on Elasticsearch 🔍</em>
</p>


## Getting Started

1) Clone the repository and install python dependencies

````
$ git clone https://github.com/AbderrahimAl/SayMySearch.git

$ cd SayMySearch

$ pip install -r requirements
````
2) Create .env file

You will need to create 3 environement varaibles to establish the connection with elasticsearch.

The easiest way is to create .env file and add the environement varaibles to it: 

````.env
ES_CLOUD_ID: <cloud id>
ES_USERNAME: elastic
ES_PASSWORD: <elasticsearch deployement password>
````

3) Run it

Run the server with

````
$ uvicorn app.api:app

INFO:     Started server process [58313]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
````

3) Check it

Open your browser at http://127.0.0.1:8000/

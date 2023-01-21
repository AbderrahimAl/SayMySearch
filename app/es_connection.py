from elasticsearch import Elasticsearch
import config

client = Elasticsearch(
    cloud_id=config.CLOUD_ID,
    basic_auth=(config.ES_USERNAME, config.ES_PASSWORD) 
)

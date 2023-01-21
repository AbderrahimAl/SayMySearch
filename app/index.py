from es_connection import client
from elasticsearch import helpers
from data import data

settings = {
    'number_of_shards': 2,
    'number_of_replicas': 1
    }
mappings = {
    'properties':{
        'club_name': {'type': 'text'}, 
        'country': {'type': 'text'}, 
        'champions': {'type': 'integer'}
    }
    }
    
client.indices.create(index='clubs_index', settings=settings, mappings=mappings, ignore=400)

helpers.bulk(client, data, index='clubs_index')
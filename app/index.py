from es_connection import client
from elasticsearch import helpers
from .data import data


index_settings = {
    'number_of_shards': 2,
    'number_of_replicas': 1
    }
index_mappings = {
    'properties':{
        'club_name': {'type': 'text'}, 
        'country': {'type': 'text'}, 
        'champions': {'type': 'integer'}
        }
    }
    
client.indices.create(index='clubs_index', settings=index_settings, mappings=index_mappings, ignore=400)

helpers.bulk(client, data, index='clubs_index')
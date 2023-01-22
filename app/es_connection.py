from elasticsearch import Elasticsearch
from .config import settings


client = Elasticsearch(
    cloud_id=settings.es_cloud_id,
    basic_auth=(settings.es_username, settings.es_password) 
)
                


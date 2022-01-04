from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch()

def generate_words():
	with open('dictionary.json', mode="r") as f:
		words = json.load(f)
		for word in words:
			if len(word) > 3:
				yield {
					"_index": "autocomplete",
					"content": word,
				}

bulk(es, generate_words())


## Stack configuration


## Index seeding
Index was seeded using [ElasticSearch Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html). 
Seeding data can be found [here](https://github.com/muteKey/elasticsearch-autocomplete/blob/master/dictionary.json). 
Seeding script can be found [here](https://github.com/muteKey/elasticsearch-autocomplete/blob/master/seed.py)

![Resulted index](https://github.com/muteKey/elasticsearch-autocomplete/blob/master/screenshots/words-index.png)

## Testing 
Autocomplete tests were performed using this curl:

```
curl -X GET "localhost:9200/_search?pretty&size=50" -H 'Content-Type: application/json' -d'
{
  "query": {
    "fuzzy": {
      "content": {
        "value": "<value>",
        "fuzziness": "2",
        "max_expansions": 3,
        "prefix_length": 0,
        "transpositions": false,
        "rewrite": "scoring_boolean"
      }
    }
  }
}
'
```

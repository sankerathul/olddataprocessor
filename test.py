from elasticsearch import Elasticsearch
import logging # for debugging purposes
import requests

# import 'json' to convert strings to JSON format
import json

# import the correct library depending on the Python version
try:
    # Python 2
    import httplib as http_client
except (ImportError, ModuleNotFoundError) as error:
    # Python 3
    print ("Python 3: Importing http.client:", error, '\n')
    import http.client as http_client


# function for the cURL requests
def elasticsearch_curl(uri='http://localhost:9200/', json_body='', verb='get'):
    # pass header option for content type if request has a
    # body to avoid Content-Type error in Elasticsearch v6.0
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # make HTTP verb parameter case-insensitive by converting to lower()
        if verb.lower() == "get":
            resp = requests.get(uri, headers=headers, data=json_body)
        elif verb.lower() == "post":
            resp = requests.post(uri, headers=headers, data=json_body)
        elif verb.lower() == "put":
            resp = requests.put(uri, headers=headers, data=json_body)

        # read the text object string
        try:
            resp_text = json.loads(resp.text)
        except:
            resp_text = resp.text

        # catch exceptions and print errors to terminal
    except Exception as error:
        print ('\nelasticsearch_curl() error:', error)
        resp_text = error

    # return the Python dict of the request
    # print ("resp_text:", resp_text)
    return resp_text


request_body = '''
{
  "from" : 0, "size" : 50,
  "query": {
    "bool":{
        "must_not":{
            "exists":{
                "field":"Categories.query_categories"
            }
        }
    }
  }
}
'''

response = elasticsearch_curl(
        'http://18.130.251.121:9200/_search?pretty',
        verb='get',
        json_body=request_body
)

docs = response["hits"]["hits"]

print(len(docs))


for doc in docs:
    print(doc)
    print("\n\n")
#     doc_id = doc["_id"]
#     doc_index = doc["_index"]
#     search_term = doc["_source"]["search_query"]
#     data = doc["_source"]


    # url = "http://slicetopiccategorisation-env-1.eba-2adpwmuq.us-east-2.elasticbeanstalk.com/categorize"

    # req ={
    # "_id": "someid123",
    # "queries": [search_term],
    # "country": "GB",
    # "language": "English",
    # "key": "c2xpY2UgdG9waWMgY2F0ZWdvcml6YXRpb24ga2V5",
    # "do_spell_correction": "false",
    # "consider_synonyms": "false"
    # }

    # req = json.dumps(req)

    # headers = {
    #     'Content-Type': 'application/json',
    # }

    # res = requests.post(url, headers=headers,data=req)
    
    # res = json.loads(res.text)
    # categories = res["query_categories"]
    # data["Categories"] = categories
    # data = json.dumps(data)

    # res = elasticsearch_curl(
    #     'http://18.130.251.121:9200/{}/_doc/{}?pretty'.format(doc_index,doc_id),
    #     verb='put',
    #     json_body=data)

    # print(data)
    # print("\n")
    # print(res)
    # print(doc_id,search_term)
    # print(categories)

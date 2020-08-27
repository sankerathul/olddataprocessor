from elasticsearch import Elasticsearch
import logging # for debugging purposes
import requests
from urllib.parse import urlparse

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



doc = {
    "browsing_url": "https://www.yahoo.com/store/apps/details?id=com.miui.securitycenter",
    "user_uuid": "asdfasdfasdf",
    "input": {
      "type": "log"
    },
    "source": "/home/ubuntu/shared_files/test_file.txt",
    "offset": 2440,
    "@version": "1",
    "search_query": "which is best whisky",
    "@timestamp": "2020-08-27T08:00:57.032Z",
    "timestamp_string": "1595479713622",
    "prospector": {
      "type": "log"
    },
    "tags": [
      "beats_input_codec_plain_applied",
      "_dateparsefailure"
    ]
  }

doc = json.dumps(doc)

res = elasticsearch_curl(
        'http://18.130.251.121:9200/logstash-2020.08.27/_doc/7ZbvLnQBhweWSk-ZKOLf?pretty',
        verb='put',
        json_body=doc)

print("\n")
print(res)

# request_body = '''
# {
#   "size" : 5,
#   "query": {
#     "bool": {
#       "should": [
#         {
#           "exists": {
#             "field": "browsing_url"
#           }
#         },
#         {
#           "bool": {
#             "must_not": [
#               {
#                 "exists": {
#                   "field": "Categories.query_categories"
#                 }
#               }
#             ]
#           }
#         }
#       ]
#     }
#   }
# }
# '''

# response = elasticsearch_curl(
#         'http://18.130.251.121:9200/_search?pretty',
#         verb='get',
#         json_body=request_body
# )

# docs = response["hits"]["hits"]

# print(len(docs))


# for doc in docs:
#     doc_id = doc["_id"]
#     doc_index = doc["_index"]
#     search_term = doc["_source"]["search_query"]
#     data = doc["_source"]

#     browse_url = doc["_source"]["browsing_url"]
#     browse_uri = urlparse(browse_url)
#     browse_host = browse_uri.hostname

#     if browse_host == 'www.google.com':

#         url = "http://slicetopiccategorisation-env-1.eba-2adpwmuq.us-east-2.elasticbeanstalk.com/categorize"

#         req ={
#         "_id": "someid123",
#         "queries": [search_term],
#         "country": "GB",
#         "language": "English",
#         "key": "c2xpY2UgdG9waWMgY2F0ZWdvcml6YXRpb24ga2V5",
#         "do_spell_correction": "false",
#         "consider_synonyms": "false"
#         }

#         req = json.dumps(req)

#         headers = {
#             'Content-Type': 'application/json',
#         }

#         res = requests.post(url, headers=headers,data=req)
        
#         res = json.loads(res.text)
#         categories = res["query_categories"]
#         data["Categories"] = categories
#         data = json.dumps(data)

#         res = elasticsearch_curl(
#             'http://18.130.251.121:9200/{}/_doc/{}?pretty'.format(doc_index,doc_id),
#             verb='put',
#             json_body=data)

#         # print(data)
#         print("\n")
#         print(res)
#         print("Doc Updated with Categories")
#         print(doc_id,search_term)
#         # print(categories)

#     else:
#         data["Categories"] = "None"
#         data = json.dumps(data)
#         res = elasticsearch_curl(
#             'http://18.130.251.121:9200/{}/_doc/{}?pretty'.format(doc_index,doc_id),
#             verb='put',
#             json_body=data)
#         print("\n")
#         print(res)
#         print("Doc Updated with out Categories")
#         print(doc_id,search_term)


        
    

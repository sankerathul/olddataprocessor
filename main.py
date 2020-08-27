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

# set the debug level
http_client.HTTPConnection.debuglevel = 1

# initialize the logging to have the debugger return information
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# store the DEBUG information in a 'requests_log' variable
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


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
  "query": {
    "exists": {
      "field": "Categories"
    }
  }
}
'''

response = elasticsearch_curl(
        'http://18.130.251.121:9200/_search?pretty',
        verb='get',
        json_body=request_body
)

print ('RESPONSE 3:', type(response), '\n\n')

response = response["hits"]["hits"]

for key in response:
    print(type(key))
    print(key)    
#print(type(response[key]))
    #print(response[key])
    print("\n\n")






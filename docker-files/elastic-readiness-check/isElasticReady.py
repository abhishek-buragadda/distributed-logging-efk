import time

import os
import requests


def isElasticSearchReady():
    elasticHost = os.getenv("ELASTICSEARCH_HOST")
    elasticPort = os.getenv("ELASTICSEARCH_PORT")
    elasticUrl = "http://{0}:{1}/_cluster/health".format(elasticHost, elasticPort)
    isElasticReady = False
    while isElasticReady != True:
        print("elastic url: " + elasticUrl)
        try:
            r = requests.get(elasticUrl)
            jsonResponse = r.json()
            isElasticReady = jsonResponse["status"] == "green"  and  jsonResponse["number_of_data_nodes"] > 0
        except:
            print("Elasticsearch Not Ready... Retrying")
            isElasticReady = False
        if isElasticReady:
            print("Elasticsearch is ready ")
        else:  
            print("sleeping for 3 sec..")
            time.sleep(3)


isElasticSearchReady()

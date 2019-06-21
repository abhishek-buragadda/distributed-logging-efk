import time

import os
import requests


def checkIndices():
    elasticHost = os.getenv("FLUENT_ELASTICSEARCH_HOST")
    elasticPort = os.getenv("FLUENT_ELASTICSEARCH_PORT")
    elasticUrl = "http://{0}:{1}/".format(elasticHost, elasticPort)
    indices = ["esmaster","required-index-name"]  #give all required index names in this array.
    isElasticReady = False
    while isElasticReady != True:
        indexCheck = True
        for index in indices:
            print("url: " + elasticUrl + index)
            try:
                r = requests.head(elasticUrl + index)
                indexCheck &= (r.status_code == 200)
            except:
                print("Not able to reach elasticsearch ...")
                indexCheck = False
                break
        print("All Indices Ready :" + str(indexCheck))
        isElasticReady = indexCheck
        if isElasticReady == False:
            print("Elasticsearch Not Ready... Retrying")
            time.sleep(3)

    return isElasticReady


checkIndices()

import logging
import random
import sys
import json

async def index_windows(es, params):
    # Make changes to ingest different documents
    logger = logging.getLogger("index_windows")
    # result = await es.perform_request(method="POST", path="/windows/_doc/" + str(random.randint(0, sys.maxsize)) + "?refresh",
    json_objects = []
    # try:
    for _ in range(80):
        index_object = {
            "index": {
                "_index": "windows",
                "_id": str(random.randint(0, sys.maxsize))
            }
        }
        data_object = params["data"]
        # logger.info("Megha data " + data_object)
        json_objects.append(json.dumps(index_object))
        # logger.info("Megha index_object " + json_objects[0])
        json_objects.append(data_object)
        # logger.info("Megha index_object " + json_objects[1])
    json_request = '\n'.join(json_objects) + '\n'
    # logger.info("Megha " + json_request)
    result = await es.perform_request(method="POST", path="/windows/_bulk?refresh", body=json_request)
    logger.info("request_status:" + str(result))
    # except Exception as e:
    #     logger.info("Exception " + str(e))
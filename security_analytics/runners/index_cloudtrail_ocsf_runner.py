import logging
import random
import sys


async def index_cloudtrail_ocsf(es, params):
    logger = logging.getLogger("index_cloudtrail_ocsf")
    result = await es.perform_request(method="POST",
                                      path="/cloudtrail_ocsf1/_doc/" + str(random.randint(0, sys.maxsize)) + "?refresh",
                                      body=str(params["data"]))
    logger.info("request_status:" + str(result))

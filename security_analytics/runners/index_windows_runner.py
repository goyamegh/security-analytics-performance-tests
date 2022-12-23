import logging
import random
import sys


async def index_windows(es, params):
    logger = logging.getLogger("index_windows")
    result = await es.perform_request(method="POST", path="/windows/_doc/" + str(random.randint(0, sys.maxsize)) + "?refresh",
                                      body=str(params["data"]))
    logger.info("request_status:" + str(result))
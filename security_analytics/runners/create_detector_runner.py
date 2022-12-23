import logging


async def create_detector(es, params):
    logger = logging.getLogger("create_detector")
    result = await es.perform_request(method="POST", path="/_plugins/_security_analytics/detectors", body=str(params["data"]))
    logger.info("request_status:" + str(result))

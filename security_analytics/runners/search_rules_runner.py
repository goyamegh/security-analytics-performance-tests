import logging


async def search_rules(es, params):
    logger = logging.getLogger("search_rules")
    result = await es.perform_request(method="POST",
                                      path="/_plugins/_security_analytics/rules/_search?pre_packaged=true",
                                      body=str(params["data"]))
    logger.info("request_status:")

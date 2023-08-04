import logging
import json

collect_findings = []


async def search_findings(es, params):
    logger = logging.getLogger("search_findings")
    result = await es.perform_request(method="GET",
                                      path="/_plugins/_security_analytics/findings/_search?detector_id=66rzsokBBPpYdgZKgVdW&size=5000&sortString=timestamp&sortOrder=desc")
    logger.info("request_status:" + str(result.body["total_findings"]))

    if int(str(result.body["total_findings"])) > 0:
        new_findings = []
        for finding in result.body["findings"]:
            new_findings.append(finding["id"])

        final_findings = []
        for finding in new_findings:
            if finding not in collect_findings:
                final_findings.append(finding)

        print("no. of new findings generated:" + str(len(collect_findings)) + "-" + str(len(final_findings)))
        collect_findings.clear()
        collect_findings.extend(final_findings)

        return {
            "weight": 1,
            "unit": "ops",
            "no_of_new_findings": len(final_findings)
        }
    else:
        return {
            "weight": 1,
            "unit": "ops",
            "no_of_new_findings": 0
        }

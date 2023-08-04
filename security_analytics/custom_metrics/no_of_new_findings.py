import certifi
from elasticsearch import Elasticsearch


class NoOfNewFindings:
    def __init__(self):
        self.es = Elasticsearch("https://<ip>:80", basic_auth=("<user>", "<passwd>"), verify_certs=False)

    def get_metric(self):
        result = self.es.perform_request(method="POST",
                                         path="/rally-metrics*/_search",
                                         body="""{
                                                  "size": 0,
                                                  "query": {
                                                    "match": {
                                                      "operation": "search-findings"
                                                    }
                                                  },
                                                  "aggs": {
                                                    "avg_findings": {
                                                      "avg": {
                                                        "field": "meta.no_of_new_findings"
                                                      }
                                                    }
                                                  }
                                                }""",
                                         headers={"Content-Type": "application/json"}
                                         )
        print("avg. no. of new findings generated:" + str(result["aggregations"]["avg_findings"]["value"]))


if __name__ == "__main__":
    NoOfNewFindings().get_metric()

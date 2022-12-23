class SearchRulesParamSource:
    def __init__(self, track, params, **kwargs):
        self._params = params

    def params(self):
        with open("security_analytics/data/search_rules.json", "r") as f:
            return {"data": f.read()}

    def partition(self, partition_index, total_partitions):
        return self
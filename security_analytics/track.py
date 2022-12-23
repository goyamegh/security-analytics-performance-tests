from security_analytics.runners import create_detector_runner
from security_analytics.runners import search_rules_runner
from security_analytics.runners import index_windows_runner
from security_analytics.param_sources.create_detector_param_source import CreateDetectorParamSource
from security_analytics.param_sources.search_rules_param_source import SearchRulesParamSource
from security_analytics.param_sources.index_windows_param_source import IndexWindowsParamSource


def register(registry):
    registry.register_runner("create-detector-api", create_detector_runner.create_detector, async_runner=True)
    registry.register_runner("search-rules-api", search_rules_runner.search_rules, async_runner=True)
    registry.register_runner("index-windows", index_windows_runner.index_windows, async_runner=True)
    registry.register_param_source("create-detector-param-source", CreateDetectorParamSource)
    registry.register_param_source("search-rules-param-source", SearchRulesParamSource)
    registry.register_param_source("index-windows-param-source", IndexWindowsParamSource)

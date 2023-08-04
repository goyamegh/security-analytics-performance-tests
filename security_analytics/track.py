from security_analytics.runners import create_detector_runner
from security_analytics.runners import search_rules_runner
from security_analytics.runners import search_findings_runner
from security_analytics.runners import index_windows_runner
from security_analytics.runners import index_cloudtrail_ocsf_runner
from security_analytics.param_sources.create_detector_param_source import CreateDetectorParamSource
from security_analytics.param_sources.search_rules_param_source import SearchRulesParamSource
from security_analytics.param_sources.index_windows_param_source import IndexWindowsParamSource
from security_analytics.param_sources.index_cloudtrail_ocsf_param_source import IndexCloudtrailOCSFParamSource


def register(registry):
    registry.register_runner("create-detector-api", create_detector_runner.create_detector, async_runner=True)
    registry.register_runner("search-rules-api", search_rules_runner.search_rules, async_runner=True)
    registry.register_runner("index-windows", index_windows_runner.index_windows, async_runner=True)
    registry.register_runner("search-findings-api", search_findings_runner.search_findings, async_runner=True)
    registry.register_runner("index-cloudtrail-ocsf", index_cloudtrail_ocsf_runner.index_cloudtrail_ocsf, async_runner=True)
    registry.register_param_source("create-detector-param-source", CreateDetectorParamSource)
    registry.register_param_source("search-rules-param-source", SearchRulesParamSource)
    registry.register_param_source("index-windows-param-source", IndexWindowsParamSource)
    registry.register_param_source("index-cloudtrail-ocsf-param-source", IndexCloudtrailOCSFParamSource)

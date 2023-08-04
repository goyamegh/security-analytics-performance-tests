elastic/rally extension for Opensearch Security-Analytics plugin
================================================================

## Reference

- [Opensearch-Security-Analytics](https://github.com/opensearch-project/security-analytics)
- [Elastic/rally](https://github.com/elastic/rally)

## Install the extension

```
git clone
pip install esrally
```

A small modification is required to run `esrally` against `Opensearch`. see https://github.com/sbcd90/rally/commit/af34c3a7db40a74db0a3750cb944d4d062afb9f4

## Use the extension

### List all tracks & challenges

```commandline
esrally list tracks --track-path="security_analytics"
```

### Show info of the track

```commandline
esrally info --track-path="security_analytics"
```

### Rally report config in `rally.ini`

```commandline
[reporting]
datastore.type = elasticsearch
datastore.host = <os-ip>
datastore.port = 80
datastore.secure = true
datastore.ssl.verification_mode = none
datastore.user = <user>
datastore.password = <passwd>
```

### Run race against a remote Opensearch cluster

```commandline
esrally race --target-hosts=cluster-ip:80 --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'<user>',basic_auth_password:'<passwd>'" --pipeline=benchmark-only --challenge=search-findings-api --track-path="security_analytics"
```

## Extend the extension with new performance test scenarios

- [Add runner](security_analytics/runners)

- [Add Param Source](security_analytics/param_sources)

- [Register runner & param source](security_analytics/track.py)

- [Add challenge for the perf test scenario](security_analytics/challenges)

- [Add operation for the perf test scenario](security_analytics/operations)

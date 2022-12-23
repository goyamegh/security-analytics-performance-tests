elastic/rally extension for Opensearch Security-Analytics plugin
================================================================

## Reference

[Opensearch-Security-Analytics](https://github.com/opensearch-project/security-analytics)

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

### Run race against a remote Opensearch cluster

```commandline
esrally race --target-hosts=127.0.0.1:39159 --pipeline=benchmark-only --challenge=create-detector-api --track-path="security_analytics"
```

## Extend the extension with new performance test scenarios

- [Add runner](security_analytics/runners)

- [Add Param Source](security_analytics/param_sources)

- [Register runner & param source](security_analytics/track.py)

- [Add challenge for the perf test scenario](security_analytics/challenges)

- [Add operation for the perf test scenario](security_analytics/operations)
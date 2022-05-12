# scrapyd-config

[![PyPI](https://img.shields.io/pypi/v/scrapyd-config?color=blue&label=PyPI&logo=PyPI&logoColor=white)](https://pypi.org/project/scrapyd-config/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scrapyd-config?logo=python&logoColor=white)](https://www.python.org/) [![codecov](https://codecov.io/gh/ilias-ant/scrapyd-config/branch/main/graph/badge.svg?token=2H0VB8I8IH)](https://codecov.io/gh/ilias-ant/scrapyd-config) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ilias-ant/scrapyd-config/CI)](https://github.com/ilias-ant/scrapyd-config/actions/workflows/ci.yml) 
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/scrapyd-config?color=orange)](https://www.python.org/dev/peps/pep-0427/)

Generate `scrapyd.conf` files, dynamically.

The idea is to be able to declare (in a simple way) the desired scrapyd configuration per environment, and then let
`scrapyd-config` generate the necessary `scrapyd.conf` for you. No need to maintain lots of `scrapyd.conf` files depending
on the de purpose of the environment.

## Install

The recommended installation is via `pip`:

```bash
pip install scrapyd-config
```

## Quick Usage

This is basically a CLI that can generate `scrapyd.conf` files, to be utilized by your scrapyd webservice.

All you have to is declare how your `scrapyd.conf` files should like on each defined environment 
(e.g. `staging`, `production`), through a simple `scrapyd-config.yml` file:

```yaml
version: "1"

base:
  scrapyd:
    max_proc: 0
    max_proc_per_cpu: 4
    finished_to_keep: 100
    ...

  services:
    schedule.json: scrapyd.webservice.Schedule
    cancel.json: scrapyd.webservice.Cancel
    ...


development:
  scrapyd:
    max_proc_per_cpu: 2

  services:
    schedule.json: scrapyd.webservice.MyCustomSchedule
    ...


staging:
  scrapyd:
    max_proc_per_cpu: 8

  services:
    schedule.json: scrapyd.webservice.MyCustomSchedule
    ...


production:
  scrapyd:
    max_proc_per_cpu: 64

  services:
    schedule.json: scrapyd.webservice.MyCustomProductionSchedule
    ...
```

Yes, you are writing a configuration file in order to solve your configuration file issues. Simple and stupid, but it works.

Then you can:

```shell
scrapyd-config generate --env production
```
and a `scrapyd.conf` will be generated, based on the `base` + `production` properties (with simple overrides).

In the same fashion, you can declare any environment you like through the yml file and then use the CLI command 
`generate` to materialize the configuration file.

## How to contribute

If you wish to contribute, [this](CONTRIBUTING.md) is a great place to start!

## License

Distributed under the [Apache-2.0 license](LICENSE).

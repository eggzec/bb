![bb](https://raw.githubusercontent.com/eggzec/bb/master/assets/bb-banner.png)

# bb

Bitbucket Cloud CLI and Python SDK.

Project conventions and generation workflow live in `CLAUDE.md`.
The deprecation system design lives in `CUSTOM_DEPRECATION_SYSTEM.md`.
Active work tracking lives in `TODO.md`.

Live smoke tests are opt-in:

`BB_RUN_LIVE_SMOKE=1 uv run pytest tests/cloud/test_live_sdk_smoke.py -q -s`

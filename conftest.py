"""Pytest bootstrap for the SDK test suite.

The SDK tests use absltest helpers, but the presubmit invokes pytest.
Parse absl's global flags before any absltest temporary-directory helpers run.
"""

from absl import flags


if not flags.FLAGS.is_parsed():
  flags.FLAGS(["pytest"])

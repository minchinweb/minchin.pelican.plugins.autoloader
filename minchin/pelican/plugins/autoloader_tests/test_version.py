import pytest

from minchin.pelican.plugins import autoloader
from minchin.pelican.plugins.autoloader import pelican_namespace_plugin_support

test_versions = [
    ("3.7.1", False),
    ("4.2.0", False),
    ("4.5.0", True),
    ("4.10.2", True),
    ("4.11.0.post0", True),
]


@pytest.mark.parametrize("ver, expected", test_versions)
def test_namespace_support(monkeypatch, ver, expected):

    monkeypatch.setattr(autoloader, "pelican_version", ver)

    rtn = pelican_namespace_plugin_support()

    assert rtn is expected

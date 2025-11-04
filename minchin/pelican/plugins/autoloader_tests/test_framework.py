import pytest


def test_do_nothing():
    """This test should always pass."""
    assert True


@pytest.mark.xfail(strict=True)
def test_fail_nothing():
    """This test should always fail (as expected)."""
    assert False

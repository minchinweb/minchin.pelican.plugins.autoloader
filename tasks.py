import sys

from invoke.tasks import task

try:
    from minchin.releaser import make_release  # noqa: F401
except ImportError:
    print("[WARN] minchin.releaser not installed.")

try:
    import pytest
except ImportError:
    pass


@task
def run_tests(ctx):
    """Run the `pytest` suite."""

    # https://docs.pytest.org/en/stable/how-to/usage.html#calling-pytest-from-python-code
    sys.exit(
        pytest.main(
            [
                "minchin",
            ]
        )
    )

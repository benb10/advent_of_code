import pytest


def pytest_addoption(parser):
    parser.addoption(
        "-R", "--max-runtime", action="store", type=float, default=1, help="Only run tests with runtime <= N seconds"
    )


def pytest_collection_modifyitems(config, items):
    max_runtime = config.getoption("--max-runtime")
    if max_runtime is None:
        return

    for item in items:
        marker = item.get_closest_marker("runtime")
        if marker is None:
            # if test has no marker, assume it is fast
            continue
        runtime = marker.args[0]
        if runtime > max_runtime:
            item.add_marker(pytest.mark.skip(reason=f"runtime {runtime}s exceeds max-runtime {max_runtime}s"))

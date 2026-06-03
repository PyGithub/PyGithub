from . import Cli


def pytest_addoption(parser):
    parser.addoption("--keep", action="store_true", help="keep intermediate test results")
    parser.addoption("--approve", action="store_true", help="approve any actual results as expected")


def pytest_configure(config):
    if config.getoption("keep", default=False):
        Cli.keepMode()
    if config.getoption("approve", default=False):
        Cli.approveMode()

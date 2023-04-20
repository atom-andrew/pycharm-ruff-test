import time

import pytest
from pycharm_ruff_test.bar import BAR  # there should be a blank line above this


@pytest.autouse('foo')
def test_foo():
    time.sleep(0.1)
    print(BAR)

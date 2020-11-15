"""
Test Main
---------
"""

import devchallenge


def test_project_defines_author_and_version():
    """
    Test author and version
    """
    assert hasattr(devchallenge, '__author__')
    assert hasattr(devchallenge, '__version__')

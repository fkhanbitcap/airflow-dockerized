"""
Test Main
---------
"""

import src


def test_project_defines_author_and_version():
    """
    Test author and version
    """
    assert hasattr(src, '__author__')
    assert hasattr(src, '__version__')

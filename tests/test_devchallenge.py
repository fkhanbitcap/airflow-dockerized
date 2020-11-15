import devchallenge as devchallenge


def test_project_defines_author_and_version():
    assert hasattr(devchallenge, '__author__')
    assert hasattr(devchallenge, '__version__')

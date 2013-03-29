pytest_plugins = "kotti"

from pytest import fixture


@fixture
def settings_events(config, request):
    """ Sets up event handlers for settings.
    """
    config.scan('kotti_settings.tests.test_events')
    return config

from pytest import fixture

pytest_plugins = "kotti"


@fixture
def settings_events(config, request):
    """ Sets up event handlers for settings.
    """
    config.scan('kotti_settings.tests.test_events')
    return config

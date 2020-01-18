import os

import app.settings as settings


def test_base_dir():
    assert os.path.exists(settings.BASE_DIR)


def test_config_is_dict():
    assert isinstance(settings.DEFAULT_CONFIG, dict)


def test_version_is_string():
    assert isinstance(settings.PROGRAM_VERSION, str)
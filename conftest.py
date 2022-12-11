import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import qa_guru_python_20_mobile_2_appium.utils.selene.patch_selector_strategy  # noqa
    import qa_guru_python_20_mobile_2_appium.utils.selene.patch_element_mobile_commands  # noqa
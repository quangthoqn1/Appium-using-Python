import pytest
from appium import webdriver

@pytest.fixture
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "app": "/tmp/app.apk",
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

def test_open_app(driver):
    assert driver.is_app_installed("com.example.android")

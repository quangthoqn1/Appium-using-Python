import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "nightwatch-android-11",
        "automationName": "UiAutomator2",
        "app": "D:/Automation-Mobile/app/android/Android-MyDemoAppRN.1.3.0.build-244.apk",
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

def test_open_app(driver):
    driver.activate_app("com.saucelabs.mydemoapp.rn")
    assert driver.current_package == "com.saucelabs.mydemoapp.rn"
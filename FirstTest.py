from appium import webdriver

desired_cap= {
    "appium:deviceName": "emulator-5554",
    "platformName": "Android",
    "appium:app": "C:\\Users\\godknows_velocityinc\\Downloads\\pointsAfrica.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

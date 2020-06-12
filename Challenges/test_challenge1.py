import time

from selenium.webdriver.common.keys import Keys


def test_go_to_google(driver):
    driver.get('https://google.com')
    assert 'Google' in driver.title
    element = driver.find_element_by_xpath("//input[@name='q']")
    element.send_keys("puppies")
    element.send_keys(Keys.RETURN)
    assert 'puppies' in driver.title




import pytest
from assertpy import assert_that
import selenium
from selenium import webdriver
import time


@pytest.mark.smoke
def test_abc():
    abc = "123"
    assert_that(abc).is_equal_to("123")


@pytest.mark.smoke
def test_browser():
    browser = webdriver.Chrome()
    browser.get("https://duckduckgo.com/")
    time.sleep(10)
    browser.quit()

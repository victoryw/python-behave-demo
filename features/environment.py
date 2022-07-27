import logging

from behave import fixture, use_fixture
from behave.log_capture import capture
from selenium import webdriver
import chromedriver_binary


def before_all(context):
    context.config.setup_logging(logging.INFO)

def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context, timeout=10)

@capture
def after_scenario(context, scenario):
    logging.info(scenario.name)


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    chrome = webdriver.Chrome(chromedriver_binary.chromedriver_filename)
    context.browser = chrome
    yield context.browser
    context.browser.close()
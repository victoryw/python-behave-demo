from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def wait_page_load(context):
    WebDriverWait(context.browser, 10).until(
        ec.presence_of_all_elements_located((By.ID, 'sb_form_q'))
    )


def search_box(context):
    return context.browser.find_element(By.ID, 'sb_form_q')

def search_box_value(context):
    return search_box(context).get_attribute('value')
from selenium.webdriver.common.by import By


def open(context):
    context.browser.get("https://www.bing.com/");


def search_box(context):
    return context.browser.find_element(By.ID, 'sb_form_q')

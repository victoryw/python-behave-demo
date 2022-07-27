from assertpy import assert_that
from behave import *

import page_object.BingHomePage as BingHomePage
import page_object.BingSearchResultPage as BingSearchResultPage

use_step_matcher("re")


@given("I was on the Bing Index")
def step_impl(context):
    BingHomePage.open(context)


@when('I search for a "(?P<keyword>.*)" keyword')
def step_impl(context, keyword):
    search_box = BingHomePage.search_box(context)
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.submit()


@then('I will find out the "(?P<keyword>.*)" in the search result page\'s input box')
def step_impl(context, keyword):
    BingSearchResultPage.wait_page_load(context)

    assert_that(BingSearchResultPage.search_box_value(context)).is_equal_to(keyword)

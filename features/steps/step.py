from behave import *

use_step_matcher("re")


@given('I search for a "(?P<type>.*)" book')
def step_impl(context, type):
    switcher = {
        "valid": "success",
        "invalid": "failure"
    }
    context.response = switcher.get(type)


@then('the result page will include "(?P<text>.*)"')
def step_impl(context, text):
    assert context.response == text;

from behave import *

use_step_matcher("parse")


@given("I search for a valid book")
def step_impl(context):
    context.response = "success"


@then('the result page will include "{text}"')
def step_impl(context, text):
    assert context.response == text;


@given("I search for a invalid book")
def step_impl(context):
    context.response = "failure"
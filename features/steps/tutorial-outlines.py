from behave import *

use_step_matcher("re")


@given("I put (?P<thing>.+) in a blender,")
def step_impl(context, thing):
    print('given is {0}'.format(thing))


@when("I switch the blender on")
def step_impl(context):
    print('when')


@then("it should transform into (.+)")
def step_impl(context, arg0):
    print('then is {0}'.format(arg0))

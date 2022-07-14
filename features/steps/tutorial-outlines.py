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


class Model:
    def __init__(self):
        self.user = {}

    def add_user(self, name, department):
        self.user[name] = department

    def find_user(self, name):
        return list(filter(lambda x: (x == name), self.user.values()))


@given("a set of specific users")
def step_impl(context):
    context.model = Model()
    for row in context.table:
        context.model.add_user(name=row['name'], department=row['department'])


@when("we count the number of people in each department")
def step_impl(context):
    pass


@then('we will find two people in "Silly Walks"')
def step_impl(context):
    out_list = context.model.find_user("Silly Walks")
    assert len(out_list) == 2


@step('we will find one person in "Beer Cans"')
def step_impl(context):
    out_list = context.model.find_user("Beer Cans")
    assert len(out_list) == 1

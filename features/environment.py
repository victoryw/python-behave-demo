import logging

from behave.log_capture import capture


def before_all(context):
    context.config.setup_logging(logging.INFO)


@capture
def after_scenario(context, scenario):
    logging.info(scenario.name)

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from log import logger
from event import Event

colorama_init()

class Policy(object):
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def add_rule(self, rule):
        self.rules.apppend(rule)

    def run(self, event: Event):
        logger.info(f"running policy: \"{self.name}\"")
        for rule in self.rules:
            # TODO(rajiv): make use of event.data for profit?
            if rule.event.kind == event.kind:
                logger.debug(f"rule: '{rule.name}' is meant for {event}")
                rule.apply()
            else:
                logger.debug(f"{Fore.RED}rule: '{rule.name}' not meant for {event}{Style.RESET_ALL}")

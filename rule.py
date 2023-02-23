from log import logger

from action import Noop

class Rule(object):
    def __init__(self, name, event, action, cond):
        self.name = name
        self.action = action
        self.event = event
        self.cond = cond
        self.noop = Noop(self.event.kind)

    def apply(self):
        if self.cond():
            logger.debug(f"condition: {self.cond} evaluated to True")
            self.action.do()
        else:
            logger.debug(f"condition: {self.cond} evaluated to False")
            self.noop.do()


    def __str__(self):
        return f"""Rule(name: {self.name} event:{self.event} action:{self.action} cond: {self.cond})"""

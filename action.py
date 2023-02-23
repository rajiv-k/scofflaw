from log import logger
from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self):
        ...

    def __str__(self):
        return f"Action(...)"

    @abstractmethod
    def do(self, *args, **kwargs):
        ...

class Noop(Action):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    def __str__(self):
        return f"Noop(...)"

    def do(self, *args, **kwargs):
        logger.debug(f"{self.ctx}: No change required")

class ScaleUp(Action):
    def __init__(self, args):
        super().__init__()
        self.args = args
    def do(self):
        logger.debug(f"cluster was scaled up: args: {self.args}")

class ScaleDown(Action):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def do(self):
        logger.debug(f"cluster was scaled down: args: {self.args}")


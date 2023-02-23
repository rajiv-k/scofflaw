from log import logger
from abc import ABC, abstractmethod

class Cond(ABC):
    def __init__(self, desc):
        self.desc = desc
    def __str__(self):
        return f"""Cond(desc:{self.desc})"""

    @abstractmethod
    def __call__(self):
        ...

class Wife(Cond):
    def __init__(self, desc, name):
        super().__init__(desc)
        self.name = name

    def __str__(self):
        return f"""Cond::Wife(name:{self.name})"""

    def __call__(self):
        logger.debug(f"{self.name} is True")
        return True

class Might(Cond):
    def __init__(self, desc, name):
        super().__init__(desc)
        self.name = name

    def __str__(self):
        return f"""Cond::Might(name:{self.name})"""

    def __call__(self):
        logger.debug(f"{self.name} is True")
        return True

class Me(Cond):
    def __init__(self, desc, name):
        super().__init__(desc)
        self.name = name

    def __str__(self):
        return f"""Cond::Me(name:{self.name})"""

    def __call__(self):
        logger.debug(f"{self.name} is False")
        return False

class Gt(Cond):
    def __init__(self, left, right):
        super().__init__("greater_than")
        self.left = left
        self.right = right
        self.name = "gt"

    def __str__(self):
        return f"""Cond::Gt(name:{self.name} left:{self.left} right:{self.right})"""

    def __call__(self):
        val = self.left > self.right
        logger.debug(f"evaluated {self}: {val}")
        return val

class Eq(Cond):
    def __init__(self, left, right):
        super().__init__("equality")
        self.left = left
        self.right = right
        self.name = "eq"

    def __str__(self):
        return f"""Cond::Eq(name:{self.name} left:{self.left} right:{self.right})"""

    def __call__(self):
        val = self.left == self.right
        logger.debug(f"evaluated {self}: {val}")
        return val

class Lt(Cond):
    def __init__(self, left, right):
        super().__init__("less_than")
        self.left = left
        self.right = right
        self.name = "lt"

    def __str__(self):
        return f"""Cond::Lt(name:{self.name} left:{self.left} right:{self.right})"""

    def __call__(self):
        val = self.left < self.right
        logger.debug(f"evaluated {self}: {val}")
        return val


class Not(Cond):
    def __init__(self, of):
        super().__init__("not")
        self.of = of

    def __str__(self):
        return f"""Cond::Not(of: {self.of})"""

    def __call__(self):
        val = not self.of()
        logger.debug(f"evaluated {self}: {val}")
        return val



class Or(Cond):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"""Cond::OR(({self.left}), ({self.right}))"""

    def __call__(self):
        val = self.left() or self.right()
        logger.debug(f"evaluated {self}: {val}")
        return val


class And(Cond):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"""Cond::AND(({self.left}), ({self.right}))"""

    def __call__(self):
        # logger.debug(f"evaluating {self.left} AND {self.right}")
        val = self.left() and self.right()
        logger.debug(f"evaluated {self}: {val}")
        return val

class Any(Cond):
    def __init__(self, *conds):
        self.conds = conds

    def __str__(self):
        return f"""Cond::Any({self.conds})"""

    def __call__(self):
        val = any([cond() for cond in self.conds])
        logger.debug(f"evaluated {self}: {val}")
        return val




from event import Event

class The(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(The, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Engine(object, metaclass=The):
    def __init__(self, policies):
        self.policies = policies

    def on_event(self, event: Event):
        for policy in self.policies:
            policy.run(event)


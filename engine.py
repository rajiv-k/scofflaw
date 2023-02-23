from event import Event

class Engine(object):
    def __init__(self, policies):
        self.policies = policies

    def on_event(self, event: Event):
        for policy in self.policies:
            policy.run(event)




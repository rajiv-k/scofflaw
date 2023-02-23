#!/usr/bin/env python3
from log import logger
from policy import Policy
from rule import Rule
from action import ScaleUp
from condition import Cond, Me, Or, And, Might, Gt, Lt, Eq, Not, Any
from event import Event, OutOfMemoryEvent, NoSpaceLeftOnDeviceEvent
from engine import Engine


if __name__ == '__main__':
    c1 = Might("might", "Almighty")
    e1 = NoSpaceLeftOnDeviceEvent(data={"device": "/dev/sdb"})
    a1 = ScaleUp({"instance": 1})
    rule1 = Rule(name="rule-1", event=e1, action=a1, cond=c1)

    c2 = And(Gt(5, 3), And(Not(Eq(4, 3)), Lt(4, 6)))
    e2 = OutOfMemoryEvent()
    a2 = ScaleUp({"instance": 2})
    rule2 = Rule(name="rule-2", event=e2, action=a2, cond=c2)

    policy = Policy("scale_infra_for_sale_policy", [rule1, rule2])
    eng = Engine([policy])
    eng.on_event(OutOfMemoryEvent(data={"msg": "killed by OOM"}))

    aaa = Any(Lt(5, 3), Lt(3, 1), Eq(3, 4))
    print(f"any result: {aaa()}")


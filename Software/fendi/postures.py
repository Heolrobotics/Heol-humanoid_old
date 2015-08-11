import time

from pypot.primitive import Primitive
from pypot.primitive.utils import Sinus, SimplePosture


class StandPosture(SimplePosture):
    @property
    def target_position(self):
        pos = dict([(m.name, 0.) for m in self.robot.motors])
        pos['m43'] = pos['m53'] = 90
        return pos


class Wave(Primitive):
    def setup(self):
        for m in self.robot.arm_r:
            m.compliant = False

    def run(self):
        self.robot.goto_position({
            'm21': 120,
            'm22': 45,
            'm23': 0,
            'm24': 30,
            }, 1, wait=True)

        self.robot.m24.moving_speed = 0
        s = Sinus(self.robot, 25., [self.robot.m24], amp=50, offset=30, freq=0.75)
        s.start()
        time.sleep(3)
        s.stop()

        self.robot.goto_position({
            'm21': 0,
            'm22': 0,
            'm23': 0,
            'm24': 0,
            }, 1, wait=True)

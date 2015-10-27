from poppy.creatures import AbstractPoppyCreature

from .postures import StandPosture, Wave


class HeolHumanoid(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot.attach_primitive(StandPosture(robot, 2.), 'stand')
        robot.attach_primitive(Wave(robot), 'wave')

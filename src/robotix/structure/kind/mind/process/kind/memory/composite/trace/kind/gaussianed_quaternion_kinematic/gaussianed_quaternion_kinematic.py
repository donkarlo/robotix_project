from functools import cache

from physix.quantity.decorator.distributed.gaussianed import Gaussianed
from physix.quantity.decorator.timed import Timed
from physix.quantity.kind.dynamic.kinematic.pose_twist_kinematic import PoseTwistKinematic
from physix.quantity.kind.dynamic.kinematic.pose.orientation.orientation import Orientation
from physix.quantity.kind.dynamic.kinematic.pose.orientation.quaternion import Quaternion
from physix.quantity.kind.dynamic.kinematic.pose.pose import Pose
from physix.quantity.kind.dynamic.kinematic.pose.position.position import Position
from physix.quantity.kind.dynamic.kinematic.twist.angular import Angular
from physix.quantity.kind.dynamic.kinematic.twist.linear import Linear
from physix.quantity.kind.dynamic.kinematic.twist.twist import Twist
from robotix.structure.kind.mind.process.kind.memory.composite.trace.kind.core.kind import Kind
from utilix.data.kind.dic.dic import Dic
from utilix.oop.klass.klass import Klass


class GaussianedQuaternionKinematic(Kind):
    """
    """
    def __init__(self):
        super().__init__("gaussianed_quaternion_kinematic")

    @cache
    def get_schema(self) -> Dic:
        gaussianed_klass_path = Klass(Gaussianed).get_module_path()
        timed_klass_path = Klass(Timed).get_module_path()
        kinematic_klass_path = Klass(PoseTwistKinematic).get_module_path()
        pose_klass_path = Klass(Pose).get_module_path()
        position_klass_path = Klass(Position).get_module_path()
        orientation_klass_path = Klass(Orientation).get_module_path()
        quaternion_klass_path = Klass(Quaternion).get_module_path()
        twist_klass_path = Klass(Twist).get_module_path()
        linear_twist_klass_path = Klass(Linear).get_module_path()
        angular_twist_klass_path = Klass(Angular).get_module_path()

        trace_kind_schema = \
            Dic({
                timed_klass_path:
                    {kinematic_klass_path:
                        [
                            {
                                gaussianed_klass_path:
                                    {
                                        pose_klass_path:
                                            [
                                                position_klass_path,
                                                {
                                                    orientation_klass_path: quaternion_klass_path
                                                }
                                            ]
                                    }
                            },
                                {
                                    gaussianed_klass_path:
                                        {
                                            twist_klass_path:
                                                [
                                                    linear_twist_klass_path,
                                                    angular_twist_klass_path
                                                ]
                                        }
                                }
                        ]
                    }
            })
        return trace_kind_schema

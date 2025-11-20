from functools import cache

from robotix.mind.memory.trace.kind.kind import Kind
from utilix.data.kind.dic.dic import Dic


class GaussianedQuaternionKinematic(Kind):
    """
    """
    def __init__(self):
        super().__init__("GaussianedQuaternionKinematic")

    @cache
    def get_schema(self) -> Dic:
        gaussianed_klass_path = Klass(Gaussianed).get_module_path()
        timed_klass_path = Klass(Timed).get_module_path()
        kinematic_klass_path = Klass(Kinematic).get_module_path()
        pose_klass_path = Klass(Pose).get_module_path()
        position_klass_path = Klass(Position).get_module_path()
        orientation_klass_path = Klass(Orientation).get_module_path()
        quaternion_klass_path = Klass(Quaternion).get_module_path()
        twist_klass_path = Klass(Twist).get_module_path()
        linear_twist_klass_path = Klass(Linear).get_module_path()
        angular_twist_klass_path = Klass(Angular).get_module_path()

        trace_kind_schema = \
            {
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
            }
        return trace_kind_schema

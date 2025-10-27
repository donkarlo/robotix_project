from robotix.platform.ros.message.type.header.frame_id_stack import FrameIdStack
from robotix.platform.ros.message.message import Message
from robotix.platforms.ros.message.frame_sequence import FrameSequence
from robotix.platforms.ros.message.time_stamp import TimeStamp


class Header:
    def __init__(self, time_stamp: TimeStamp, frame_id_stack:FrameSequence,sequence:int):
        self._time_stamp = time_stamp
        self._frame_id_stack = frame_id_stack
        self._sequence = sequence

    def get_time_stamp(self)->TimeStamp:
        return self._time_stamp

    def get_frame_sequence(self)->FrameSequence:
        return self._frame_id_stack


    @classmethod
    def init_from_ros_message_dic(cls, dic:Dic)->"Header":
        time_stamp = TimeStamp.get_time_by_dic(dic)
        frame_id_stack = FrameIdStack.init_from_message_dic(dic)
        sequence = dic["header"]["seq"]
        return(cls(time_stamp, frame_id_stack, sequence))

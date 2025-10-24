from robotix.platforms.ros.message.frame_sequence import FrameSequence
from robotix.platforms.ros.message.time_stamp import TimeStamp


class Header:
    def __init__(self, time_stamp:TimeStamp, frame_sequence:FrameSequence):
        self._time_stamp = time_stamp
        self._frame_sequence = frame_sequence

    def get_time_stamp(self)->TimeStamp:
        return self._time_stamp

    def get_frame_sequence(self)->FrameSequence:
        return self._frame_sequence
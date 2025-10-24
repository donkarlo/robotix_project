from typing import List


class FrameSequence:
    def __init__(self, frame_list:List[str]):
        """

        Args:
            frame_list: from parent to children
        """
        self._frame_list = frame_list

    def get_frame_list(self)->List[str]:
        return self._frame_list
class Quaternion(ColVec):  # type: ignore 
    def __init__(self, qx, qy, qz, qw):
        self._qx = qx
        self._qy = qy
        self._qz = qz
        self._qw = qw
        super().__init__((self._qx, self._qy, self._qz, self._qw))

    def convert_to_euler(self)->Euler:
        pass
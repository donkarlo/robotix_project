from typing import Optional

class Command:
    def __init__(self, id:Optional[str]=None):
        """
        A short request such as increase rotation speed of rotor 4 by 10%
        - command is issuable and after issuance it is forgated

        - it is not assessable and modifiable. Once it is released, it can not be modified
        """
        self._id = id
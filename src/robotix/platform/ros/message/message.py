from utilix.data.type.dic.dic import Dic

class Message(ABC):
    def __init__(self, fields:List[Dict]):
        self._fields = fields




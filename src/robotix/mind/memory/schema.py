from functools import cache

from utilix.data.kind.dic.dic import Dic

class Schema:
    @cache
    def get_schema_dic(self)->Dic:
        return Dic\
        (
            {
                "memory": {
                    "long_term": {
                        "explicit": {
                            "auto_biographic": {},
                            "episodic": {},
                            "semantic": {}
                        }
                    },
                    "short_term": {}
                }
            }
        )
    def draw(self):
        self.get_schema_dic().draw()
if __name__ == "__main__":
    schema = Schema().draw()


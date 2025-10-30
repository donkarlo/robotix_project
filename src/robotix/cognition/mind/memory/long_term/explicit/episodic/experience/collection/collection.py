from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import List, Optional
class Collection:
    def __init__(self, member_experiences:Optional[List[Experience]]=None):
        if member_experiences is not None:
            self._members_experience = member_experiences
        else:
            self._members_experience = []

    def get_members_experience(self)->List[Experience]:
        return self._members_experience

    def __getitem__(self, index:int)->Experience:
        return self._members_experience[index]

    def add_experience(self, experience:Experience)->None:
        self._members_experience.append(experience)

    def get_experience_by_name(self, name:str)->Optional[Experience]:
        for experience in self._members_experience:
            if experience.get_name() == name:
                return experience
        return None
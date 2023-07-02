from abc import ABC, abstractmethod

from src.state import Role


class InteractionFactory(ABC):
    @abstractmethod
    def create_interaction(self, role: Role):
        pass

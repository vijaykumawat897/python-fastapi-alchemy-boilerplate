from abc import ABC, abstractmethod
from app.generated.models import Person, PersonCreate

class PersonService(ABC):
    @abstractmethod
    async def create_person(self, person: PersonCreate) -> Person:
        """Create a new person."""
        raise NotImplementedError
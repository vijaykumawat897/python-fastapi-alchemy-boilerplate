from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.generated.models import Person, PersonCreate
from app.repositories.person import PersonRepository
from app.services.person.service import PersonService

class PersonServiceImpl(PersonService):
    def __init__(self, repository: PersonRepository):
        self.repo = repository

    async def create_person(self, person: PersonCreate) -> Person:
        """Create a new person.""" 
        db_person = models.Person(**person.model_dump())    
        db_person = await self.repo.create(db_person)
        return db_person
from sqlalchemy.ext.asyncio import AsyncSession
from app import models
from app.generated.models import PersonCreate

class PersonRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, person: PersonCreate) -> models.Person:
        db_person = models.Person(**person.model_dump())
        self.db.add(db_person)
        await self.db.commit()
        await self.db.refresh(db_person)
        return db_person

    async def get(self, person_id: int) -> models.Person | None:
        return await self.db.get(models.Person, person_id)

    # async def update(self, person: models.Person, data: PersonUpdate) -> models.Person:
    #     for k, v in data.model_dump(exclude_unset=True).items():
    #         setattr(person, k, v)
    #     await self.db.commit()
    #     await self.db.refresh(person)
    #     return person

    async def delete(self, person: models.Person) -> None:
        await self.db.delete(person)
        await self.db.commit()

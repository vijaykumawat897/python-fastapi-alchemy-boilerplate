from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.generated.models import Person, PersonCreate
from app.repositories.person import PersonRepository
from app.services.person.service import PersonService
from app.services.person.service_impl import PersonServiceImpl

router = APIRouter(prefix="/persons")

def get_person_service(
    db: AsyncSession = Depends(get_db),
) -> PersonService:
    return PersonServiceImpl(repo=PersonRepository(db))

@router.post("/", response_model=Person)
async def create_person(person: PersonCreate, service: PersonService = Depends(get_person_service)):
    return await service.create_person(person)
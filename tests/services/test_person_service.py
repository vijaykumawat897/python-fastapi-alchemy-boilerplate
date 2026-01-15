import pytest
from unittest.mock import AsyncMock

from app.services.person.service_impl import PersonServiceImpl
from app.repositories.person import PersonRepository
from app.generated.models import PersonCreate
from app import models


@pytest.mark.asyncio
async def test_create_person_success():
    # Create a mocked repository
    mock_repo = AsyncMock(spec=PersonRepository)

    # Mock repo.create to return a SQLAlchemy model instance
    mock_repo.create.return_value = models.Person(
        name="Vijay", email="vijay123@test.com"
    )

    # Inject mock repository into service
    service = PersonServiceImpl(repository=mock_repo)

    payload = PersonCreate(
        name="Vijay",
        email="vijay123@test.com",
    )

    result = await service.create_person(payload)

    # Assert that repo.create was called once with a Person instance
    created_person_arg = mock_repo.create.call_args.args[0]
    assert isinstance(created_person_arg, models.Person)
    assert created_person_arg.name == "Vijay"
    assert created_person_arg.email == "vijay123@test.com"

    # Assert returned result is the mocked model
    assert result.name == "Vijay"
    assert result.email == "vijay123@test.com"


@pytest.mark.asyncio
async def test_create_person_adds_correct_model_fields():
    mock_repo = AsyncMock(spec=PersonRepository)

    # Capture the Person returned by the repository
    mock_repo.create.side_effect = lambda db_person: db_person

    service = PersonServiceImpl(repository=mock_repo)

    person_data = PersonCreate(
        name="Test User",
        email="test@example.com"
    )

    result = await service.create_person(person_data)

    # Ensure the repository was called with correct model
    added_person = mock_repo.create.call_args.args[0]

    assert isinstance(added_person, models.Person)
    assert added_person.name == "Test User"
    assert added_person.email == "test@example.com"

    # The returned person should match the model we passed to repo
    assert result.name == "Test User"
    assert result.email == "test@example.com"

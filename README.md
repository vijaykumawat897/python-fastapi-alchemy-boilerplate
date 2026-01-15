# Python FastAPI Boilerplate

A production-ready boilerplate for building FastAPI applications with SQLAlchemy, following contract-first API development principles and clean architecture patterns.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🗄️ **SQLAlchemy (Async)** - Asynchronous ORM with PostgreSQL support
- 📝 **Contract-First Development** - OpenAPI-first approach with code generation
- 🏗️ **Clean Architecture** - Layered architecture with Service/Repository pattern
- 🔄 **Alembic** - Database migration management
- 🧪 **Pytest** - Testing framework with async support
- 🔧 **Type Safety** - Full type hints and Pydantic models
- 📦 **Dependency Injection** - FastAPI's built-in DI system

## Project Structure

```
.
├── app/
│   ├── api/              # API endpoints and routers
│   │   ├── health.py     # Health check endpoint
│   │   ├── person.py     # Person endpoints (example)
│   │   └── router.py     # Main API router
│   ├── core/             # Core configuration and database
│   │   ├── config.py     # Application configuration
│   │   └── database.py   # Database setup and session management
│   ├── generated/        # Auto-generated Pydantic models from OpenAPI
│   │   └── models.py
│   ├── models/           # SQLAlchemy ORM models
│   │   ├── base.py       # Base model class
│   │   └── person.py     # Person model (example)
│   ├── repositories/     # Data access layer
│   │   └── person.py     # Person repository (example)
│   ├── services/         # Business logic layer
│   │   ├── health/       # Health service
│   │   └── person/       # Person service (interface + implementation)
│   └── main.py           # FastAPI application entry point
├── contracts/            # OpenAPI specifications
│   ├── openapi.yaml      # Main OpenAPI spec
│   ├── paths/            # API endpoint definitions
│   └── schemas/          # Data schemas
├── alembic/              # Database migrations
│   └── versions/         # Migration files
├── tests/                # Test files
│   └── services/         # Service tests
├── alembic.ini           # Alembic configuration
├── Makefile              # Convenience commands
├── pyproject.toml        # Project metadata
└── requirements.txt      # Python dependencies
```

## Architecture

The project follows a clean architecture pattern with clear separation of concerns:

1. **API Layer** (`app/api/`) - Handles HTTP requests/responses and routing
2. **Service Layer** (`app/services/`) - Contains business logic (interface + implementation)
3. **Repository Layer** (`app/repositories/`) - Handles data access operations
4. **Model Layer** (`app/models/`) - SQLAlchemy ORM models
5. **Generated Models** (`app/generated/`) - Pydantic models generated from OpenAPI specs

## Prerequisites

- Python 3.10+
- PostgreSQL database
- pip

## Installation

1. **Clone the repository** (or use this as a template)

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
make install
# or
pip install -r requirements.txt
```

4. **Set up environment variables**:
Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
TEST_DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/test_dbname
ENV=development
APP_NAME=FastAPI App
```

5. **Generate Pydantic models from OpenAPI spec**:
```bash
make generate
```

6. **Run database migrations**:
```bash
make migrate
# or
alembic upgrade head
```

## Usage

### Running the Application

```bash
make run
# or
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs` (Swagger UI)
- Alternative Docs: `http://localhost:8000/redoc` (ReDoc)

### Available Make Commands

- `make install` - Install all dependencies
- `make generate` - Generate Pydantic models from OpenAPI spec
- `make run` - Run the development server
- `make test` - Run tests
- `make migrate` - Run database migrations
- `make revision m="message"` - Create a new migration
- `make upgrade` - Upgrade database to latest migration
- `make downgrade` - Downgrade database by one migration
- `make clean` - Remove generated models

## Development Workflow

### Contract-First API Development

1. **Define your API contract** in `contracts/openapi.yaml` and related files:
   - Add endpoint definitions in `contracts/paths/`
   - Add schemas in `contracts/schemas/`

2. **Generate Pydantic models**:
```bash
make generate
```

3. **Implement the layers**:
   - Create SQLAlchemy models in `app/models/`
   - Create repository in `app/repositories/`
   - Create service interface in `app/services/{resource}/service.py`
   - Implement service in `app/services/{resource}/service_impl.py`
   - Create API endpoints in `app/api/`

4. **Create database migration**:
```bash
make revision m="add new table"
```

5. **Run migrations**:
```bash
make migrate
```

### Adding a New Resource

1. **Define the contract** in `contracts/`:
   - Add schema in `contracts/schemas/`
   - Add endpoints in `contracts/paths/`
   - Update `contracts/openapi.yaml`

2. **Generate models**:
```bash
make generate
```

3. **Create SQLAlchemy model** in `app/models/`

4. **Create repository** in `app/repositories/`

5. **Create service**:
   - Interface: `app/services/{resource}/service.py`
   - Implementation: `app/services/{resource}/service_impl.py`

6. **Create API router** in `app/api/` and add to `app/api/router.py`

7. **Create migration**:
```bash
make revision m="add {resource} table"
make migrate
```

## Testing

Run tests with:
```bash
make test
# or
pytest
```

## Database Migrations

### Create a new migration:
```bash
make revision m="description of changes"
```

### Apply migrations:
```bash
make migrate
```

### Rollback last migration:
```bash
make downgrade
```

## Configuration

Configuration is managed through environment variables and the `Config` class in `app/core/config.py`. The following variables are required:

- `DATABASE_URL` - PostgreSQL connection string (asyncpg format)
- `TEST_DATABASE_URL` - Test database connection string
- `ENV` - Environment (development/production)
- `APP_NAME` - Application name

## API Endpoints

### Health Check
- `GET /api/v1/health` - Health check endpoint

### Example: Persons
- `POST /api/v1/persons` - Create a new person

## Technologies Used

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM (async)
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **Pytest** - Testing framework
- **Uvicorn** - ASGI server
- **asyncpg** - PostgreSQL async driver
- **datamodel-code-generator** - OpenAPI to Pydantic model generation

## License

This is a boilerplate template. Customize as needed for your project.

## Contributing

This is a boilerplate project. Feel free to fork and customize for your needs.


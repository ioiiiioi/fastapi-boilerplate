# PaddyBot API

A modern FastAPI boilerplate with PostgreSQL, Redis, and comprehensive project structure.

## 🚀 Features

- **FastAPI Framework**: High-performance async API framework
- **PostgreSQL Database**: Async SQLAlchemy ORM with connection pooling
- **Redis Cache**: Async Redis client with helper utilities
- **Alembic Migrations**: Database migration management
- **Pydantic Serializers**: Type-safe request/response models
- **Docker Support**: Complete Docker Compose setup
- **Well-Structured**: Organized codebase with separation of concerns

## 📁 Project Structure

```
paddybot/
├── main.py                 # FastAPI application entry point
├── config.py              # Application configuration
├── requirements.txt       # Python dependencies
├── alembic.ini           # Alembic configuration
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── Makefile              # Convenient make commands
├── service/              # Service layer
│   ├── __init__.py
│   ├── database.py       # PostgreSQL connection & session
│   └── cache.py          # Redis connection & helpers
├── models/               # ORM Models
│   ├── __init__.py
│   ├── base.py          # Base model with common fields
│   └── user.py          # Example User model
├── utils/               # Utilities
│   ├── __init__.py
│   ├── serializers.py   # Pydantic schemas
│   ├── helpers.py       # Helper functions
│   └── exceptions.py    # Custom exceptions
└── migrations/          # Alembic migrations
    ├── env.py
    ├── script.py.mako
    ├── README
    └── versions/
```

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   cd /home/hexboi/Documents/personal/paddybot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   make install
   # or
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   make dev
   # or
   uvicorn main:app --reload
   ```

### Docker Development

1. **Start all services**
   ```bash
   make docker-up
   # or
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   docker-compose logs -f app
   ```

3. **Stop services**
   ```bash
   make docker-down
   # or
   docker-compose down
   ```

## 🗄️ Database Migrations

### Create a new migration
```bash
make migrate-create MSG="description of changes"
# or
alembic revision --autogenerate -m "description of changes"
```

### Apply migrations
```bash
make migrate
# or
alembic upgrade head
```

### Rollback migration
```bash
alembic downgrade -1
```

### View migration history
```bash
alembic history
```

## 📝 Environment Variables

Create a `.env` file in the root directory:

```env
# Application
APP_NAME=PaddyBot
DEBUG=True

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/paddybot
DB_ECHO=False

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🧪 API Endpoints

### Health Check
```http
GET /health
```

Response:
```json
{
  "status": "healthy"
}
```

### Root
```http
GET /
```

Response:
```json
{
  "message": "Welcome to PaddyBot API"
}
```

## 🏗️ Usage Examples

### Creating a new endpoint

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from service.database import get_db

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    # Your logic here
    pass
```

### Using Redis Cache

```python
from service.cache import CacheService

# Set cache
await CacheService.set("key", "value", expire=3600)

# Get cache
value = await CacheService.get("key")

# Delete cache
await CacheService.delete("key")
```

### Creating a new model

```python
from models.base import BaseModel
from sqlalchemy import Column, String

class YourModel(BaseModel):
    __tablename__ = "your_table"
    
    name = Column(String(100), nullable=False)
```

### Creating a serializer

```python
from utils.serializers import BaseSerializer

class UserSerializer(BaseSerializer):
    id: int
    username: str
    email: str
```

## 🔧 Make Commands

```bash
make install        # Install dependencies
make run           # Run the application
make dev           # Run in development mode (with reload)
make docker-up     # Start Docker containers
make docker-down   # Stop Docker containers
make migrate       # Run database migrations
make migrate-create MSG='message' # Create new migration
make test          # Run tests
make lint          # Run linter
make format        # Format code
make clean         # Clean cache files
```

## 🔒 Security

- Change `SECRET_KEY` in production
- Use strong passwords for database
- Enable HTTPS in production
- Update CORS settings in `main.py`
- Never commit `.env` file

## 📚 Tech Stack

- **FastAPI** - Modern web framework
- **PostgreSQL** - Relational database
- **Redis** - Caching and session storage
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **Docker** - Containerization

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Redis Documentation](https://redis.io/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)


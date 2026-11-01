# FastAPI Application

A clean, production-ready FastAPI service organized with a standard folder structure, PostgreSQL with SQLAlchemy ORM, Alembic migrations, JWT authentication, and modern tooling with `uv`.

---

## 📁 Project Structure

```text
FastAPI_111023/
├── .github/
│   └── workflows/
│       └── docker.yml          # GitHub Actions CI/CD for Docker build & publish
├── alembic/
│   ├── versions/               # Database migration versions
│   ├── env.py                  # Alembic environment and model metadata configuration
│   └── script.py.mako          # Migration template
├── app/
│   ├── core/                   # Configuration, Database engine, Security helpers
│   │   ├── config.py           # Centralized settings & environment variables
│   │   ├── database.py         # SQLAlchemy engine (with pool_pre_ping=True), SessionLocal, Base, get_db
│   │   ├── security.py         # Password hashing & JWT token generation
│   │   └── __init__.py
│   ├── models/                 # SQLAlchemy database models
│   │   ├── user.py             # User ORM model
│   │   └── __init__.py
│   ├── schemas/                # Pydantic schemas (Request / Response models)
│   │   ├── token.py            # Token schemas
│   │   ├── user.py             # User schemas (Create, Update, Out)
│   │   └── __init__.py
│   ├── repositories/           # Data access layer (pure SQL/ORM queries)
│   │   ├── user.py             # User database query functions
│   │   └── __init__.py
│   ├── services/               # Business logic layer (hashing, workflows, rules)
│   │   ├── auth.py             # Authentication service
│   │   ├── user.py             # User service
│   │   └── __init__.py
│   ├── routers/                # API route controllers
│   │   ├── auth.py             # Authentication endpoints (/auth/login)
│   │   ├── users.py            # User management endpoints (/users)
│   │   └── __init__.py
│   ├── dependencies.py         # Auth dependency (get_current_user)
│   ├── main.py                 # FastAPI application factory & /health endpoint
│   └── __init__.py
├── tests/                      # Automated test suite
│   ├── conftest.py             # Pytest fixtures and TestClient setup
│   ├── test_health.py          # API health check test
│   └── __init__.py
├── .dockerignore               # Docker build ignore rules
├── .env.example                # Example environment configuration template
├── .gitignore                  # Git ignore rules for Python, virtualenv, and caches
├── .python-version             # Python version pin (3.14)
├── alembic.ini                 # Alembic configuration
├── Dockerfile                  # Container definition
├── pyproject.toml              # Project dependencies and dev tools (Ruff, Mypy, Pytest)
├── README.md                   # Project documentation
└── uv.lock                     # Deterministic dependency lockfile
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.14+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)
- PostgreSQL database

### 1. Clone & Environment Setup

```bash
# Clone the repository
git clone <repo-url>
cd FastAPI_111023

# Copy the environment file template
cp .env.example .env
```

Edit `.env` to configure your database and secret key:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/fastapi_db
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 2. Install Dependencies

Using `uv`:

```bash
uv sync
```

---

## 🗄️ Database Migrations

Run database migrations with Alembic:

```bash
# Apply migrations to the latest revision
uv run alembic upgrade head

# Generate a new migration revision
uv run alembic revision --autogenerate -m "describe schema change"
```

---

## 💻 Running the Application

### Development Server

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Interactive API documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Testing & Code Quality

```bash
# Run test suite
uv run pytest

# Check code formatting & linting with Ruff
uv run ruff check .

# Auto-format code
uv run ruff format .
```

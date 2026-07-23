# 🌐 Astralis API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00599C?logo=fastapi&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-orchestration-2496ED?logo=docker&style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

**RESTful API for server and game management**  
Modern, fast, and type-safe API with automatic documentation, authentication, and real-time monitoring.

[🚀 Features](#-features) • [📦 Installation](#-installation) • [📖 API Docs](#-api-docs) • [🛠️ Tech Stack](#️-tech-stack)

</div>

---

## ✨ Features

### 🎮 Game Server Management
- Start/stop/restart game servers
- Real-time status and player count
- Server configuration management
- Backup and restore saves

### 🖥️ System Monitoring
- CPU, RAM, disk usage endpoints
- Temperature monitoring
- Process management
- Health checks

### 🔐 Authentication & Security
- JWT token authentication
- API key support
- Rate limiting
- CORS configuration

### 📊 Real-time Updates
- WebSocket support for live metrics
- Server status notifications
- Event-driven architecture

### 📚 Automatic Documentation
- Swagger UI at `/docs`
- ReDoc at `/redoc`
- OpenAPI 3.0 schema
- Type hints with Pydantic

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Core language |
| **FastAPI** | Web framework |
| **Pydantic** | Data validation |
| **SQLAlchemy** | Database ORM |
| **Alembic** | Database migrations |
| **JWT** | Authentication |
| **Docker** | Containerization |
| **PostgreSQL** | Database (optional) |

---

## 📦 Installation

### Prerequisites
- Python 3.11+
- Docker (optional)

### Quick Start
```bash
git clone https://github.com/Fioru12/Astralis-API.git
cd Astralis-API
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker run -d \
  --name astralis-api \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  fioru12/astralis-api:latest
```

---

## 📖 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Example Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Health check |
| `GET` | `/api/v1/system/info` | System information |
| `GET` | `/api/v1/system/metrics` | CPU, RAM, disk usage |
| `POST` | `/api/v1/server/start` | Start game server |
| `POST` | `/api/v1/server/stop` | Stop game server |
| `GET` | `/api/v1/server/status` | Server status |
| `GET` | `/api/v1/docker/containers` | List containers |
| `POST` | `/api/v1/docker/{id}/start` | Start container |

---

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DATABASE_URL` | ❌ No | PostgreSQL connection string |
| `SECRET_KEY` | ✅ Yes | JWT secret key |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | ❌ No | Token expiration (default: 30) |
| `DOCKER_SOCKET` | ❌ No | Docker socket path |
| `TELEGRAM_BOT_TOKEN` | ❌ No | For notifications |

---

## 🏗️ Architecture

```
Astralis-API/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── system.py
│   │   │   │   ├── server.py
│   │   │   │   └── docker.py
│   │   │   └── router.py
│   │   └── deps.py          # Dependencies
│   ├── core/
│   │   ├── config.py        # Settings
│   │   ├── security.py      # JWT auth
│   │   └── database.py      # DB connection
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   └── services/            # Business logic
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🧪 Testing

```bash
# Run tests
pytest tests/ -v

# With coverage
pytest --cov=app tests/
```

---

## 📈 Roadmap

- [ ] GraphQL API support
- [ ] gRPC endpoints
- [ ] Kubernetes operator
- [ ] Prometheus metrics
- [ ] OpenTelemetry tracing
- [ ] Multi-language support (i18n)

---

## 🤝 Contributing

Contributions are welcome! Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Fioru12** - [GitHub Profile](https://github.com/Fioru12)

---

<div align="center">
  <sub>Built with ❤️ for modern server management</sub>
</div>

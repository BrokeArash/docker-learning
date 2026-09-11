# Docker Learning Project

A small containerized Task Manager application built as a hands-on project for learning Docker and fundamental DevOps concepts.

> **Note:** The Task Manager itself is not intended to be a production application or a practically useful product. The application was intentionally kept simple so that the main focus could remain on Docker, containerization, networking, persistence, health checks, and CI/CD.

---

## 🎯 Project Goal

The main goal of this project was to learn Docker through a small but realistic multi-container application.

Instead of learning Docker only through isolated commands and tutorials, this project was used as a practical environment to understand how different services work together.

The project gradually introduced concepts such as:

- Docker images and containers
- Dockerfiles
- Docker Compose
- Container networking
- Environment variables
- Persistent volumes
- PostgreSQL
- Nginx
- Reverse proxying
- Health checks
- Service dependencies
- Container restart policies
- Non-root containers
- Gunicorn
- Database initialization
- GitHub Actions
- Automated testing
- GitHub Container Registry (GHCR)

The purpose was to understand **why these technologies are used and how they fit together**, rather than simply learning their commands.

---

## 🏗️ Architecture

The application consists of three main services:

```text
                    Browser
                       │
                       ▼
              ┌─────────────────┐
              │     Frontend    │
              │  Nginx + HTML   │
              └────────┬────────┘
                       │
                 /api/ │
                       ▼
              ┌─────────────────┐
              │     Backend     │
              │ Flask + Gunicorn│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    PostgreSQL   │
              │     Database    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Docker Volume  │
              │ Persistent Data │
              └─────────────────┘

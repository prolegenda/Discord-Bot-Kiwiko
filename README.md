# HelixBot

HelixBot is a modular, event-driven Discord bot platform designed for SaaS-grade scaling.

## Core goals
- Shard-aware architecture for 10k+ guild growth
- Plugin SDK with dependency resolution and hot reload lifecycle hooks
- Event bus abstraction for local + distributed messaging
- Strongly typed service container (DI) for testability and modularity
- FastAPI dashboard API for multi-tenant control planes

## High-level architecture

```text
Discord Gateway
      ↓
Shard Manager
      ↓
Core Engine
 ├── Command Router
 ├── Event Bus
 ├── Permission Engine
 ├── Plugin Loader
 ├── Service Container (DI)
 └── Cache Layer (Redis)
      ↓
Cogs / Plugins
      ↓
Database (PostgreSQL)
      ↓
Web Dashboard (FastAPI)
```

## Repository layout
- `helixbot/core`: runtime engine primitives
- `helixbot/services`: IO services (db/cache/logging/scheduling)
- `helixbot/plugins`: first-party plugin packages
- `api`: dashboard API skeleton
- `tests`: unit tests for runtime-critical modules

## Next milestones
1. Implement Discord gateway adapters and shard orchestration workers.
2. Add SQLAlchemy 2.0 async repositories + Alembic migrations.
3. Wire Redis pub/sub backend for cross-process EventBus.
4. Expand plugin SDK for command/event registration DSL.

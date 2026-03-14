# AlertForge

AlertForge is a **backend system for cryptocurrency price alerts** built with **FastAPI**, **PostgreSQL**, **JWT authentication**, **background workers**, and **Docker**.

Users can register, log in, create alerts, view their alerts, delete alerts, and automatically check whether live crypto prices meet alert conditions.

---

## Features

### Authentication
- User registration
- User login
- JWT-based authentication
- Password hashing with bcrypt
- Protected routes using bearer tokens

### Alert System
- Create cryptocurrency price alerts
- View alerts for the authenticated user
- Delete alerts owned by the authenticated user
- Store alert rules in PostgreSQL

### Alert Processing Engine
- Fetch live crypto prices from the CoinGecko API
- Compare live prices against stored alert conditions
- Mark alerts as triggered
- Save the time an alert was triggered

### Background Worker
- Automatic alert checking using APScheduler
- Runs on a timed interval without manual input

### Deployment
- Dockerized backend
- Docker Compose support
- Deployable to Render

---

## Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Passlib**
- **python-jose**
- **APScheduler**
- **Requests**
- **Docker**
- **Docker Compose**

---

## Project Structure

```bash
alertforge-backend/
│
├── app/
│   ├── core/
│   │   ├── alert_checker.py
│   │   ├── database.py
│   │   ├── price_service.py
│   │   ├── scheduler.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── alert.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── alerts.py
│   │   └── auth.py
│   │
│   ├── schemas/
│   │   ├── alert.py
│   │   └── user.py
│   │
│   └── main.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt

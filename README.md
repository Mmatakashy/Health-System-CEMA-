# Health-System-CEMA

This is a three-day project for shortlisting at CEMA Hospital. It features a health information system with:

- 🧠 **FastAPI** backend (Python)
- 🌐 **React** frontend (JavaScript)
- 🐘 **PostgreSQL** as the database

---

## 🛠️ Backend Setup (FastAPI)

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- Virtual environment

### Setup
```bash
cd health-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

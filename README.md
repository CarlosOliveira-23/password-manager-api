# 🔐 Password Manager API

A secure and open-source password manager API built with FastAPI.  
It provides user authentication, password encryption with AES-256, and a secure storage system.

---

## 🚀 Features
✅ Secure password storage with AES-256 encryption  
✅ User authentication with JWT  
✅ FastAPI-based RESTful API  
✅ Unit and integration tests with pytest  
✅ Open-source and extensible  

---

## 📂 Project Structure
```
password-manager-api/
│── app/
│   ├── models/        # Database models
│   ├── schemas/       # Pydantic schemas for data validation
│   ├── services/      # Business logic (encryption, authentication)
│   ├── routes/        # API routes
│   ├── core/          # Configurations and settings
│   ├── tests/         # Unit and integration tests
│   ├── main.py        # Entry point of the application
│── .env               # Environment variables (DO NOT COMMIT)
│── .gitignore         # Ignoring unnecessary files
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
│── docker-compose.yml # Docker setup (optional)
```
---

## ⚙️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/CarlosOliveira-23/password-manager-api
cd password-manager-api
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up the database
- Create a `.env` file and configure your **PostgreSQL database URL**:
```ini
DATABASE_URL=postgresql://user:password@localhost/password_manager
SECRET_KEY=your_secret_key
```
- Run migrations:
```bash
alembic upgrade head
```

---

## 🚀 Running the API
```bash
uvicorn app.main:app --reload
```
- Open **Swagger UI** at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Open **ReDoc** at: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Running Tests
```bash
pytest
```

---

## 📜 License
This project is licensed under the **MIT License**.

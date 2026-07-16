# 📒 Advanced Contact Book Management System

A full-stack **Contact Management Web Application** built using **Flask REST API** and **Streamlit Dashboard**.

This project upgrades a basic Python Contact Book CLI application into a modern web-based application with a separate backend and frontend architecture.

---

# 🚀 Features

## Contact Management

✅ Add new contacts  
✅ View all contacts  
✅ Update existing contacts  
✅ Delete contacts  
✅ Search contacts by name  

---

## Backend Features (Flask)

✅ REST API architecture  
✅ CRUD operations  
✅ JSON-based data storage  
✅ Flask-CORS support  
✅ API endpoints for frontend communication  

---

## Frontend Features (Streamlit)

✅ Interactive dashboard  
✅ Simple user interface  
✅ Sidebar navigation  
✅ Real-time API communication  
✅ Contact management forms  

---

# 🏗️ Project Architecture

```
Advanced-Contact-Book/

│
├── backend/
│   │
│   ├── app.py                 # Flask REST API
│   ├── database.py            # Database operations
│   ├── ContactBook.json       # Contact storage
│   ├── requirements.txt
│   └── .env
│
│
├── frontend/
│   │
│   ├── streamlit_app.py       # Streamlit UI
│   └── requirements.txt
│
│
├── README.md
├── .gitignore
├── LICENSE
└── requirements.txt
```

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- Flask-CORS
- REST API
- JSON Database


## Frontend

- Streamlit
- Requests


## Tools

- Git & GitHub
- VS Code
- Virtual Environment

---

# 🔄 Application Flow

```
User
 |
 |
Streamlit UI
 |
 |
HTTP Requests
 |
 |
Flask REST API
 |
 |
ContactBook.json
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/Advanced-Contact-Book.git
```

---

## 2. Navigate to Project

```bash
cd Advanced-Contact-Book
```

---

# 🔥 Backend Setup

Go inside backend:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask server:

```bash
python app.py
```

Backend will start:

```
http://127.0.0.1:5000
```

or if port changed:

```
http://127.0.0.1:5001
```

---

# 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

Application will open:

```
http://localhost:8501
```

---

# 🔌 API Documentation

## Base URL

```
http://127.0.0.1:5000
```

---

## 1. Get All Contacts

### GET

```
/contacts
```

Example:

```
GET /contacts
```

Response:

```json
{
    "Ashish":{
        "phone":"9876543210",
        "email":"ashish@gmail.com"
    }
}
```

---

## 2. Add Contact

### POST

```
/add
```

Request:

```json
{
    "name":"Ashish",
    "phone":"9876543210",
    "email":"ashish@gmail.com"
}
```

Response:

```json
{
    "message":"Contact Added"
}
```

---

## 3. Update Contact

### PUT

```
/update/<name>
```

Example:

```
/update/Ashish
```

Request:

```json
{
    "phone":"9999999999",
    "email":"new@gmail.com"
}
```

---

## 4. Delete Contact

### DELETE

```
/delete/<name>
```

Example:

```
/delete/Ashish
```

---

## 5. Search Contact

### GET

```
/search/<name>
```

Example:

```
/search/Ashish
```

---

# 📸 Application Preview

(Add screenshots here)

Example:

```
screenshots/
 |
 ├── dashboard.png
 ├── add-contact.png
 └── search.png
```

---

# 📦 Requirements

Backend:

```
flask
flask-cors
python-dotenv
gunicorn
```

Frontend:

```
streamlit
requests
```

---

# 🚀 Deployment

## Backend Deployment

Recommended platforms:

- Render
- Railway
- AWS EC2
- Fly.io


## Frontend Deployment

Deploy Streamlit application using:

- Streamlit Community Cloud


Deployment Architecture:

```
Streamlit Cloud
        |
        |
        API Requests
        |
        |
Render Flask API
```

---

# 🔮 Future Improvements

## Version 2

- 🔐 User Authentication
- JWT Login System
- SQLite Database
- PostgreSQL Support
- Contact Profile Images
- Import/Export CSV
- Dark Mode UI
- Responsive Design


## AI Features

Future AI integration:

- AI Contact Assistant
- Voice Contact Creation
- Smart Contact Search
- Duplicate Contact Detection
- Natural Language Queries

Example:

```
"Find my college friend's number"
```

---

# 🧠 Learning Outcomes

Through this project:

- Learned Flask API development
- Built REST APIs
- Connected frontend and backend
- Used JSON as database
- Implemented CRUD operations
- Learned full-stack Python development
- Learned deployment architecture

---

# 👨‍💻 Author

**Ashish Mewada**

AI Engineer | Python Developer | Full Stack Developer

GitHub:

```
https://github.com/ashishpatel3630-art
```

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
Social Proof Notification Micro SaaS 
Overview
This is a simple micro SaaS backend for handling real-time social proof notifications. It allows you to store and retrieve recent customer activity (e.g., purchases) for display on a frontend widget.

## Features
- Store customer purchase notifications
- Retrieve the last 5 notifications
- Uses Flask and SQLAlchemy with SQLite database

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/social-proof-saas.git
cd social-proof-saas
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
```bash
python
>>> from app import db, app
>>> with app.app_context():
>>>     db.create_all()
>>>     print("Database initialized successfully!")
>>> exit()
```

## Running the Application
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`

## API Endpoints
### 1. Add a Notification
- **Endpoint:** `/add_notification`
- **Method:** `POST`
- **Payload:**
```json
{
  "customer_name": "John Doe",
  "product": "Ebook - Marketing 101",
  "location": "New York, USA"
}
```
- **Response:**
```json
{
  "message": "Notification added successfully!"
}
```

### 2. Get Recent Notifications
- **Endpoint:** `/get_notifications`
- **Method:** `GET`
- **Response:**
```json
[
  {
    "customer_name": "John Doe",
    "product": "Ebook - Marketing 101",
    "location": "New York, USA",
    "timestamp": "2025-03-22T14:30:00"
  }
]
```

## Future Enhancements
- Add WebSocket support for real-time updates
- Deploy to cloud services (Heroku, AWS, etc.)
- Implement user authentication

## License
MIT License

---

Let me know if you need any modifications! 🚀


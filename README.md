# CUT.LY - URL Shortener

CUT.LY is a simple and efficient URL shortener built using Flask and SQLAlchemy, with Tailwind CSS for styling. This project allows users to generate short links for long URLs and track visit counts.

## 🚀 Features
- Shorten long URLs quickly
- Track the number of visits for each short link
- Custom short URLs
- Responsive design with Tailwind CSS
- Simple and clean UI

## 🛠️ Tech Stack
- **Backend**: Flask, Flask-SQLAlchemy
- **Frontend**: Tailwind CSS
- **Database**: SQLite (default), but supports PostgreSQL/MySQL

## 📂 Project Structure
```
CUT.LY/
│── app/
│   ├── templates/        # HTML templates
│   ├── __init__.py       # Flask app initialization
│   ├── models.py         # Database models
│   ├── routes.py         # URL routes and logic
│   ├── utils.py          # Utility functions
│── venv/                 # Virtual environment
│── .gitignore            # Git ignore file
│── LICENSE               # License information
│── requirements.txt      # Python dependencies
│── run.py                # Application entry point
│── urlshortener.db       # SQLite database file
```

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/cut.ly.git
cd cut.ly
```

### 2️⃣ Create a virtual environment & install dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the application
```sh
python run.py
```
The app will be available at **http://127.0.0.1:5000/**.

## 🛠️ Usage
1. Enter a long URL in the input field.
2. Click **Shorten** to generate a short URL.
3. Copy and share the short URL.
4. Track visits for each link.

## 📜 License
This project is licensed under the MIT License.

---
💡 **Inspired by tinyurl and bit.ly**


# DiPTi - NSDA Web Application with Python (Level 4)

This is a Django-based web application developed for the **DiPTi & NSDA Skill Development Program (Level 4)**. It demonstrates core backend and frontend development concepts including authentication, CRUD operations, database handling, and responsive UI.

---

## 🛠️ Step-by-Step Setup Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/skhalidmahmud/DiPTi--NSDA--Web-Application-Dev-with-Python--L-4.git
cd DiPTi--NSDA--Web-Application-Dev-with-Python--L-4
```

---

### Step 2: Create & Activate Virtual Environment

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Required Packages

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

If not:

```bash
pip install django
```

---

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

---

### Step 5: Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

---

### Step 6: Run the Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

### Step 7: Access Admin Panel

Go to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with the superuser credentials.

---

## 🧰 Technologies Used

* Python 3.x
* Django Framework
* HTML5, CSS3
* Bootstrap or Tailwind CSS
* JavaScript (optional)
* SQLite (default)

---

## 🗂️ Project Structure (Basic)

```
DiPTi--NSDA--Web-Application-Dev-with-Python--L-4/
├── app/                # Django app
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── db.sqlite3          # Default database
├── manage.py           # Django manager
└── requirements.txt    # Package dependencies
```

---

## 💡 Features

* ✅ User registration & login
* ✅ Admin dashboard
* ✅ CRUD operations
* ✅ Mobile responsive design
* ✅ Django security features

---

## 📄 Developer Notes

📘 See [`Note for Django.md`](Note%20for%20Django.md) for detailed internal documentation and learning notes.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to GitHub: `git push origin feature-name`
5. Open a pull request

---

## 📧 Contact

**Khalid Mahmud**
📩 Email: [skhalidmahmud1@gmail.com](mailto:skhalidmahmud1@gmail.com)
🔗 LinkedIn: [linkedin.com/in/skhalidmahmud](https://www.linkedin.com/in/skhalidmahmud)

---

## 🏁 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
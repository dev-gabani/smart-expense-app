🚀 Smart Expense Analyzer

Smart Expense Analyzer is a full-stack financial management web application designed to help users track, analyze, and optimize their spending behavior.

This project was built from scratch, evolving from a basic local Flask app into a fully deployed, cloud-backed Progressive Web App (PWA) with real-world backend architecture.

---

🎯 Key Features

* 🔐 User Authentication (secure login system)
* 💰 Income & Expense Tracking
* 📊 Category-based Budgeting System
* 🧠 Smart Budget Analysis (overspending detection)
* 📈 Expense Prediction System
* 💡 AI-based Financial Suggestions (rule-based)
* 📅 Monthly Summary & Insights
* 📤 Data Export (Excel reports)
* 🌐 REST API (for future mobile integration)
* 📱 Progressive Web App (installable on mobile)
* ☁️ Cloud Database (PostgreSQL on Render)

---

🧠 Tech Stack

**Backend:**

* Python
* Flask
* SQLAlchemy (ORM)
* JWT Authentication

**Frontend:**

* HTML, CSS, JavaScript (Jinja Templates)

**Database:**

* PostgreSQL (Production)
* SQLite (Local Development)

**Deployment & Tools:**

* Git & GitHub
* Render (Hosting)
* Postman (API Testing)

🏗️ Architecture

```
User → Web App (Flask) → API → Database (PostgreSQL)
```


⚙️ Key Engineering Highlights

* Implemented hybrid database configuration (SQLite locally, PostgreSQL in production)
* Handled environment-based configuration using environment variables
* Fixed PostgreSQL driver issues using `psycopg2`
* Resolved `postgres://` vs `postgresql://` compatibility issue
* Built REST API for future Android app integration
* Implemented session + token-based authentication
* Designed a modular and scalable backend structure

⚠️ Challenges Solved

* Deployment errors (500 Internal Server Error)
* Database connection issues (SQLAlchemy OperationalError)
* Environment variable configuration on Render
* Git & version control setup (including force push recovery)
* API testing errors (405, 415, authentication issues)
* Network access issues during mobile testing

🔮 Future Improvements

* Advanced AI-based recommendations
* Data visualization (charts & dashboards)
* Android mobile application
* PostgreSQL scaling & backup automation
* Improved UI/UX design

🧠 Learning Outcome

This project demonstrates the transition from beginner-level coding to building a real-world, production-style application, covering backend development, API design, deployment, debugging, and system architecture.


👨‍💻 Author

Built and designed by Dev Gabani as a full-stack learning project.

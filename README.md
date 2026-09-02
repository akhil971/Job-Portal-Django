# Job Portal — Frontend Development

A responsive job listing platform built with Django, allowing users to browse job listings, view job details, register/login, and explore companies.

## Features

- Home, About, and Contact pages
- Job listings page with individual job detail views
- Company listings page
- User registration and login pages
- Responsive HTML/CSS pages built with Django templates

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, Django Templates
- **Database:** SQLite

## Project Structure

```
job_portal/
├── manage.py
├── job_progile/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/                  # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/            # HTML templates (home, jobs, companies, login, register, etc.)
│   ├── static/                # CSS files
│   └── migrations/
└── db.sqlite3
```

## Setup Instructions

1. Clone the repository
   ```
   git clone https://github.com/akhil971/Job-Portal.git
   cd Job-Portal
   ```

2. Create and activate a virtual environment
   ```
   python -m venv env
   env\Scripts\activate      # Windows
   source env/bin/activate   # macOS/Linux
   ```

3. Install dependencies
   ```
   pip install django
   ```

4. Run migrations
   ```
   python manage.py migrate
   ```

5. Start the development server
   ```
   python manage.py runserver
   ```

## Author

**Akhil Kumar**
BCA Student | Aspiring Software Developer
[GitHub](https://github.com/akhil971) | [LinkedIn](https://linkedin.com/in/akhil-kumar-053510366)

*This project was implemented under mentor guidance as part of academic coursework.*

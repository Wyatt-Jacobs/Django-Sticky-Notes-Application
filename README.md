# Sticky Notes Application

A simple Django web application that allows users to create, view, edit, and delete sticky notes. The application demonstrates Django's Model-View-Template (MVT) architecture, form handling, URL routing, database migrations, and basic CRUD functionality.

## Features

- Create new sticky notes
- View a list of all notes
- View note details
- Edit existing notes
- Delete notes
- Automatically record the creation date and time for each note
- Responsive sticky note styled interface

## Technologies Used

- Python 3
- Django
- SQLite3
- HTML5
- CSS3

## Project Structure

```text
sticky_notes/
│
├── manage.py
├── db.sqlite3
│
├── notes/
│   ├── migrations/
│   ├── static/
│   │   └── notes/
│   │       └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   └── notes/
│   │       ├── note_list.html
│   │       ├── note_detail.html
│   │       └── note_form.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── sticky_notes/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd sticky_notes
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the application

Visit:

```text
http://127.0.0.1:8000/
```

## Database

This application uses SQLite as the default database. Database schema changes are managed using Django migrations.

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

## Author

Wyatt Jacobs

## License

This project was created for educational purposes as part of a Django development assignment.

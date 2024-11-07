# Notesapp

A simple note-taking application built with Django. This project supports Docker to ensure platform compatibility and easy deployment.

## Features

- User Authentication (Signup, Login, Logout)

- Add, View, Edit, and Delete Notes

- Django Class-Based Views

- Dockerized for easy setup and deployment

## Getting Started
### Prerequisites

- Python 3.10 or higher

- Docker and Docker Compose installed on your system

## Project setup
### 1. Clone the Repository

```bash
git clone https://github.com/stormshadow47/notesapp.git
cd notesapp-main

```

### 2. Create a Virtual Environment

```bash
python -m venv notes_env
.\notes_env\Scripts\activate # On mac or linux use 'source notes_env/bin/activate'

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Apply Migrations

```bash
python manage.py migrate

```

### 5. Run the Development Server

```bash
python manage.py runserver

```




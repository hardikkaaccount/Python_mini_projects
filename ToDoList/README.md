# To-Do List Application 📝

A simple yet functional **To-Do List** web application built with Flask and SQLAlchemy. This app allows users to manage their tasks efficiently by adding, updating, and deleting items from their to-do list.

---

## 📋 Project Overview

The **To-Do List Application** offers users a straightforward interface to manage their daily tasks. The application stores task data in an SQLite database and provides an intuitive way to interact with the list via a web browser.

---

## 🛠️ Features

- **Task Management**:
  - Add tasks to the to-do list.
  - Mark tasks as complete or incomplete.
  - Delete tasks when no longer needed.
- **Database Integration**:
  - Persistent storage of tasks using SQLite.
- **Responsive Web Pages**:
  - Easy-to-use interface with real-time updates.

---

## 🔧 Technologies Used

- **Backend**: Flask (Python).
- **Database**: SQLite (via SQLAlchemy ORM).
- **Frontend**: HTML (via Jinja2 templates), CSS (via Semantic UI).

---

## 📂 Code Structure

- **`app.py`**:
  - Main application logic.
  - Routes for task management (add, update, delete).
- **`base.html`**:
  - HTML template for rendering the to-do list and form.
- **`semantic.min.css`**:
  - Semantic UI CSS for styling.

---

## 📖 How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hardikkaaccount/Python_mini_projects.git
   cd Python_mini_projects/ToDoList

Simple Flask Todo App using SQLAlchemy and SQLite database.

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```

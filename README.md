# Flask TODO App

A simple CRUD (Create, Read, Update, Delete) TODO application built with **Flask**.  
This project is primarily for me to learn and get familiar with the Flask framework.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)

---

## Features

- Add new TODO items
- View all TODO items
- Update existing TODO items
- Delete TODO items
- Minimal and clean interface for learning purposes

---

## Tech Stack

- **Python 3.8**
- **Flask** – web framework
- **HTML/CSS** – frontend
- **SQLite** – database for storing TODO items

---

## Installation

Follow these steps to run the project locally:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/flask-todo-app.git](https://github.com/your-username/flask-todo-app.git)
    cd flask-todo-app
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    -   **Mac/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**

    ```bash
    python app.py
    ```

6.  Open your browser and go to: `http://127.0.0.1:5000/`

---

## Project Structure

```text
flask-todo-app/
│
├─ app.py           # Main Flask application
├─ templates/       # HTML templates for pages
│   ├─ index.html
│   ├─ edit.html
│   └─ ...
├─ static/          # CSS, JS, and other static files
├─ requirements.txt # Python dependencies
└─ README.md        # Project documentation

```

## Usage
- Open the homepage to see all TODO items.
- Use the form to add a new TODO item.
- Click edit to update an existing item.
- Click delete to remove an item.

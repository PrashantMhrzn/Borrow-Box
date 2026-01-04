# BorrowBox

## Project Overview

**BorrowBox** is a full-featured Library Management System API built with Django REST Framework. It allows libraries to efficiently manage books, authors, genres, and user interactions like 
borrowing, reserving, and reviewing books. The system supports authenticated user actions with dynamic fine calculation for overdue books, and robust data filtering and pagination for seamless usage.

## Features

- User authentication with permission controls
- CRUD operations on book, authors, genre, reserve, borrow and review with role based authentication
- Borrowing system with dynamic fine calculation
- Reservation system with conflict checking
- Review system for books
- Filtering and searching books by title, author, or genre
- Pagination for efficient data handling
- API responses formatted for RESTful consumption
- Comprehensive Admin panel for full database management
## Setup Instructions

### Prerequisites

- Python 3.12+
- PostgreSQL (or SQLite for testing)
- `pip` (Python package manager)

### Installation

```bash
# Clone the repo
git clone https://github.com/your-username/borrowbox.git
# Go into the cloned directory
cd borrowbox
# Enable virtual environment
python -m venv venv
source venv/bin/activate
# For Windows
venv\Scripts\activate
# Install the packages
pip install -r requirements.txt
# Other Setups
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Visit the app: http://127.0.0.1:8000/ \
Admin panel: http://127.0.0.1:8000/admin/

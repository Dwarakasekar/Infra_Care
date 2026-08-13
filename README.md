# InfraCare

InfraCare is a Django-based web application designed to provide centralized infrastructure-related information, assistance, and support through multiple integrated modules.

The project brings together features such as an AI-powered chatbot, infrastructure advisory, disaster management tools, weather information, tracking, sustainability, and user support in a single web application.

## Overview

Infrastructure-related information and support can often be distributed across different sources and systems. InfraCare was developed as a centralized platform that allows users to access different infrastructure-related services and information through a single Django-based web application.

The application is structured using Django's project and application architecture, with individual Django apps responsible for different functional areas.

## Key Features

### AI Chatbot

The chatbot module provides an interactive interface for users to ask questions and receive assistance.

Key capabilities include:

* Interactive user conversations
* Infrastructure-related assistance
* Question-and-answer functionality
* Integration with the Django application
* User-friendly chatbot interface

### Infrastructure Advisor

The advisor module is designed to provide infrastructure-related guidance and information to users.

It can be used to organize and present relevant infrastructure information through the web application.

### Disaster Toolkit

The disaster toolkit provides resources and information related to disaster situations.

The module is intended to help users access useful information and tools related to disaster preparedness and response.

### Weather Module

The weather module provides weather-related information through the application.

This can help users access weather information alongside other infrastructure-related services.

### Tracking Module

The tracking module provides functionality related to tracking and monitoring within the application.

### Sustainability Module

The sustainability module focuses on sustainability-related information and resources.

### Support Module

The support module provides users with access to support-related functionality within the application.

### Quiz/Data Module

The project also includes quiz-related data stored in YAML format and can be used by the application for interactive content.

## Technologies Used

### Backend

* Python
* Django
* Django ORM

### Database

* SQLite

### Frontend

* HTML
* CSS
* JavaScript
* Django Templates

### Data

* YAML

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

## Django Architecture

InfraCare follows the standard Django architecture.

The application is organized into multiple Django applications, with each application handling a specific feature or functional area.

```text
                         InfraCare
                             |
                     Django Project
                             |
        ------------------------------------------------
        |          |          |          |              |
     Advisor    Chatbot   Disaster    Weather       Support
                           Toolkit
        |          |          |          |              |
        ------------------------------------------------
                             |
                     Django ORM
                             |
                          SQLite
```

## Project Structure

```text
InfraCare/
│
├── advisor/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── chatbot/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── disaster_toolkit/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── infracare/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
├── support/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── sustain/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── templates/
│   └── ...
│
├── track/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── weather/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── manage.py
├── quiz_data.yaml
├── requirements.txt
└── README.md
```

## Understanding the Database

InfraCare uses Django ORM to interact with the database.

Instead of writing SQL queries manually for every database operation, Django models are used to define the application's data structure.

The basic flow is:

```text
Django Models
      ↓
Django ORM
      ↓
SQL Queries
      ↓
SQLite Database
```

For example, a Django model can define fields and relationships, and Django ORM handles the conversion between Python objects and database records.

This allows database operations to be performed using Python and Django ORM while Django handles the underlying SQL operations.

## Why Django ORM?

Django ORM provides several advantages for the project:

* Database interaction through Python
* Reduced need for manually written SQL queries
* Model-based database design
* Easier database migrations
* Integration with Django applications
* Cleaner and maintainable database code

## Application Flow

The general flow of the application is:

```text
User
  ↓
Web Browser
  ↓
Django URL Routing
  ↓
Django Views
  ↓
Application Logic
  ↓
Django ORM
  ↓
SQLite Database
  ↓
Response
  ↓
Django Template
  ↓
Web Browser
```

## Installation

### 1. Clone the Repository

Clone this repository to your local machine using the repository URL available on GitHub.

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd Infra_Care
```

### 2. Create a Virtual Environment

Create a new Python virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

After activation, the terminal should show:

```text
(.venv)
```

### 4. Install Dependencies

Install the packages required by the project:

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

Run Django migrations:

```bash
python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

Open the address in a web browser to access InfraCare.

## Django Management Commands

Some useful commands for working with the project are:

### Check the Django project

```bash
python manage.py check
```

### Run migrations

```bash
python manage.py migrate
```

### Create migrations

```bash
python manage.py makemigrations
```

### Start the development server

```bash
python manage.py runserver
```

### Create a Django superuser

```bash
python manage.py createsuperuser
```

## Database Migrations

Django migrations are used to keep the database structure synchronized with the Django models.

The general workflow is:

```text
Modify models.py
      ↓
python manage.py makemigrations
      ↓
Migration files created
      ↓
python manage.py migrate
      ↓
Database structure updated
```

## Git and GitHub Workflow

The project is maintained using Git and GitHub.

The basic development workflow is:

```text
Make changes
     ↓
git add .
     ↓
git commit -m "Description of changes"
     ↓
git push
     ↓
GitHub
```

Example:

```bash
git add .
git commit -m "Added chatbot improvements"
git push
```

## Environment and Security

The Python virtual environment is not included in the repository.

Instead, the required Python packages are listed in:

```text
requirements.txt
```

This allows developers to create their own virtual environment and install the required dependencies.

Sensitive information such as:

* API keys
* Passwords
* Secret keys
* Environment variables
* Database credentials

should not be committed to the repository.

## Future Improvements

Possible future improvements for InfraCare include:

* Improving the AI chatbot capabilities
* Adding authentication and user profiles
* Expanding infrastructure-related datasets
* Improving disaster response functionality
* Adding more real-time information sources
* Improving the user interface and accessibility
* Adding automated testing
* Deploying the application to a cloud platform
* Improving database scalability
* Adding analytics and reporting features

## Learning Outcomes

Developing InfraCare provided practical experience with:

* Python web development
* Django framework
* Django project and app architecture
* Django ORM
* Database design
* SQLite
* URL routing
* Django views
* Templates
* Static files
* Database migrations
* Git and GitHub
* Virtual environments
* Modular application development

## Project Status

**Status:** Prototype / Development Project

InfraCare was developed as a modular Django web application demonstrating how multiple infrastructure-related features can be integrated into a single platform.

## Author

Dwaraka J. S.

B.Tech – Information Technology

---

## License

This project is intended for educational and portfolio purposes.

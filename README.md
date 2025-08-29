# Thesis Management System

A Thesis Management System built with pure Python that helps manage students, courses, and thesis projects efficiently.  
It provides a structured way to store, retrieve, and manage data related to academic theses, users, and associated files.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Data Files](#data-files)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Configuration](#configuration)
- [Development Notes](#development-notes)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Overview
This project is designed to support academic institutions in managing the lifecycle of theses.  
It provides a minimal yet extendable backend for handling:
- Students and their details
- Courses offered
- Thesis records
- File management (PDFs, images, etc.)

The project uses JSON files as the database, making it lightweight and easy to set up without external services.

---

## Features
- User management stored in `users.json`
- Course management via `courses.json`
- Thesis records handled in `theses.json`
- File storage for PDFs and images
- Clear separation of code modules for models, services, and helpers
- Pure Python with no external dependencies

---

## Project Structure
```
thesis_management_system/
│
├── main.py                 # Entry point of the application
│
├── data/                   # JSON-based "database"
│   ├── courses.json
│   ├── theses.json
│   └── users.json
│
├── files/                  # Supporting documents
│   ├── images/
│   └── pdfs/
│
└── src/                    # Core source code
    ├── functions.py        # Utility functions
    ├── models.py           # Data models
    └── services.py         # Business logic
```

---

## Data Files
The project uses JSON files located in the `data/` folder:
- `users.json`   — user records (students, supervisors, admins)
- `courses.json` — course data
- `theses.json`  — thesis records

---

## Requirements
- Python 3.8 or newer
- Terminal or command prompt
- Read/write access to the project directory

No external packages are required.

---

## Installation
1. Clone the repository
```
git clone https://github.com/MehdiAhmadiyan/Thesis-Management-System.git
```

2. Change into the project directory
```
cd Thesis-Management-System
```

3. Verify Python version
```
python --version
```

---

## How to Run
Run from the project root:
```
python main.py
```

---

## Configuration
- Data files are located in `data/`
- Supporting files are stored under `files/pdfs/` and `files/images/`
- Update file paths in `main.py` or `src/` if the structure is changed

---

## Development Notes
- `models.py` defines Python classes and data models
- `services.py` contains operations and business logic
- `functions.py` contains helper utilities
- Run the program from the project root so paths resolve correctly

---

## Future Improvements
- Use a database backend instead of JSON
- Add authentication and roles
- Create a web or GUI interface
- Add JSON schema validation
- Implement reporting (PDF/CSV)
- Add automated testing

---

## Contributing
1. Fork the repository  
2. Create a feature branch  
3. Commit changes with clear messages  
4. Open a pull request  

---

## Contact
Author: Mehdi Ahmadiyan  
GitHub: https://github.com/MehdiAhmadiyan

---

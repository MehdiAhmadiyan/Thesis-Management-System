# 🎓 Thesis Management System

A **Thesis Management System** built with **pure Python** that helps manage students, courses, and thesis projects efficiently.  
It provides a structured way to store, retrieve, and manage data related to academic theses, users, and associated files.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Data Files](#data-files)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 📖 Overview
This project is designed to support academic institutions in managing the **lifecycle of theses**.  
It provides a minimal yet extendable backend for handling:
- Students and their details  
- Courses offered  
- Thesis records  
- File management (PDFs, images, etc.)  

The project uses **JSON files as the database**, making it lightweight and easy to set up without external dependencies.

---

## 🚀 Features
- **User Management**  
  Store and retrieve user details from `users.json`.

- **Course Management**  
  Manage available courses via `courses.json`.

- **Thesis Management**  
  Handle thesis records (students, supervisors, topics, etc.) via `theses.json`.

- **File Handling**  
  Organize related files in dedicated directories for **PDFs** and **Images**.

- **Service-Oriented Architecture**  
  Core logic divided into `functions.py`, `models.py`, and `services.py` for modularity and reusability.

---

## 📂 Project Structure
thesis_management_system/
│── main.py # Entry point of the application
│
├── data/ # Data storage (JSON-based "database")
│ ├── courses.json
│ ├── theses.json
│ └── users.json
│
├── files/ # File storage (supporting documents)
│ ├── images/
│ └── pdfs/
│
├── src/ # Core source code
│ ├── functions.py # Utility and helper functions
│ ├── models.py # Data models for users, courses, theses
│ ├── services.py # Business logic and services
│ └── pycache/ # Auto-generated cache files


---

## 🗄️ Data Files
The project uses JSON files located in the **`data/`** folder as its database:
- **`users.json`** → Stores user information (students, professors, admins, etc.)  
- **`courses.json`** → Contains course data  
- **`theses.json`** → Stores thesis records and metadata  

---

## ⚙️ Installation
1. Clone this repository:
git clone https://github.com/MehdiAhmadiyan/Thesis-Management-System.git
2. Navigate into the project folder:
cd Thesis-Management-System
3. Ensure you have **Python 3.8+** installed:
python --version


No external dependencies are required — this project uses only **Python’s standard library**.

---

## ▶️ How to Run
From the root folder of the project, run:
python main.py


---

## 🌱 Future Improvements
- Add a proper **database backend** (e.g., SQLite, PostgreSQL).  
- Build a **web-based interface** using Flask/Django or a frontend framework.  
- Implement **authentication & role-based access** (students, supervisors, admins).  
- Enhance **file management** (uploads, secure storage).  
- Provide **report generation** in PDF/Excel formats.  

---

## 🤝 Contributing
Contributions are welcome!  
If you’d like to improve the system, feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📬 Contact
**Author:** Mehdi Ahmadiyan  
📧 [mahdiahmadiyan13@gmail.com]  
🔗 [GitHub Profile](https://github.com/MehdiAhmadiyan)

---

# 📚 Thesis Management System

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Repo Size](https://img.shields.io/github/repo-size/MehdiAhmadiyan/Thesis-Management-System.svg)](https://github.com/MehdiAhmadiyan/Thesis-Management-System)
[![Stars](https://img.shields.io/github/stars/MehdiAhmadiyan/Thesis-Management-System?style=social)](https://github.com/MehdiAhmadiyan/Thesis-Management-System/stargazers)

A **Thesis Management System** built with pure Python 🐍 that helps manage students, courses, and thesis projects efficiently.  
It provides a structured way to store, retrieve, and manage data related to academic theses, users, and associated files.

---

## 📑 Table of Contents
- [✨ Overview](#-overview)
- [🚀 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🗄️ Data Files](#️-data-files)
- [⚙️ Requirements](#️-requirements)
- [📥 Installation](#-installation)
- [▶️ How to Run](#️-how-to-run)
- [🔧 Configuration](#-configuration)
- [🛠️ Development Notes](#️-development-notes)
- [🌟 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)
- [📬 Contact](#-contact)

---

## ✨ Overview
This project is designed to support academic institutions 🎓 in managing the **lifecycle of theses**.  
It provides a minimal yet extendable backend for handling:
- 👨‍🎓 Students and their details  
- 📘 Courses offered  
- 📄 Thesis records  
- 🗂️ File management (PDFs, images, etc.)  

The project uses **JSON files as the database**, making it lightweight and easy to set up without external dependencies.

---

## 🚀 Features
- 👥 **User Management** via `users.json`  
- 📚 **Course Management** with `courses.json`  
- 📝 **Thesis Records** stored in `theses.json`  
- 🖼️ **File Storage** for PDFs and images  
- 🧩 Modular design with models, services, and functions  
- 💡 Pure Python — **no external dependencies**

---

## 📂 Project Structure
```
thesis_management_system/
│
├── main.py                 # ▶️ Entry point of the application
│
├── data/                   # 🗄️ JSON-based "database"
│   ├── courses.json
│   ├── theses.json
│   └── users.json
│
├── files/                  # 📂 Supporting documents
│   ├── images/
│   └── pdfs/
│
└── src/                    # ⚙️ Core source code
    ├── functions.py        # 🔧 Utility functions
    ├── models.py           # 🧱 Data models
    └── services.py         # 🛠️ Business logic
```

---

## 🗄️ Data Files
The project uses JSON files located in the **`data/`** folder:
- `users.json`   — 👥 user records (students, supervisors, admins)  
- `courses.json` — 📘 course data  
- `theses.json`  — 📝 thesis records  

---

## ⚙️ Requirements
- Python **3.8+** 🐍  
- Terminal or command prompt  
- Read/write permissions to the project directory  

✅ No external packages are required.

---

## 📥 Installation
1. Clone the repository  
```
git clone https://github.com/MehdiAhmadiyan/Thesis-Management-System.git
```

2. Navigate into the project directory  
```
cd Thesis-Management-System
```

3. Verify Python version  
```
python --version
```

---

## ▶️ How to Run
Run the system from the project root:  
```
python main.py
```

---

## 🔧 Configuration
- Data files are located in `data/`  
- Supporting files are stored under `files/pdfs/` and `files/images/`  
- Update file paths in `main.py` or `src/` if the structure is changed  

---

## 🛠️ Development Notes
- `models.py` defines Python classes and data models 🧱  
- `services.py` contains business logic 🛠️  
- `functions.py` provides utility helpers 🔧  
- Run the program from the project root to ensure paths resolve correctly  

---

## 🌟 Future Improvements
- Replace JSON storage with a proper database (SQLite/PostgreSQL) 🗄️  
- Add authentication & role-based access 🔐  
- Build a web interface 🌐  
- Implement validation & schema checking ✔️  
- Generate reports in PDF/CSV 📊  
- Add automated testing 🧪  

---

## 🤝 Contributing
Contributions are welcome! 🚀  
1. Fork the repository  
2. Create a feature branch  
3. Commit changes with clear messages  
4. Open a pull request  

---

## 📬 Contact
**Author:** Mehdi Ahmadiyan  
🔗 GitHub: [MehdiAhmadiyan](https://github.com/MehdiAhmadiyan)  

---

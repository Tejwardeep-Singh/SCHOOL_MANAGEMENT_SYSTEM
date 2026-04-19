# 🏫 School Management System (CLI Version)

## 📌 Overview

This project is a **Command-Line Interface (CLI) based School Management System** built using **Python and MySQL**.

It was developed as a **Class 12 final project** to demonstrate database integration, logical structuring, and real-world system simulation.

The system allows management of:

* Students
* Teachers
* Payroll
* Leave requests
* School information

👉 The entire application runs in the terminal using menu-driven interaction.

---

## 🚀 Features

### 🔐 Authentication System

* Head Login (Admin)
* Staff Login
* Student Login

---

### 👨‍🏫 Head (Admin) Functionalities

* Manage staff records
* Manage student records
* Generate payroll
* Approve/reject leave requests
* Manage school infrastructure
* Handle admission forms and bills
* View grants and FAQs

---

### 👨‍🎓 Student Functionalities

* View profile
* Apply for leave

---

### 👨‍🏫 Staff Functionalities

* View profile
* Apply for leave
* Approve student leave
* View salary details
* Access student data

---

### 📊 Additional Modules

* School infrastructure details
* Events and calendar
* CBSE news & government policies
* Feedback system
* Fee structure
* Quiz system (GK, Science, History, etc.)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Libraries Used:**

  * `mysql.connector`
  * `tabulate`
  * `datetime`

---

## ⚙️ Setup Instructions

### 1️⃣ Install Required Libraries

```bash
pip install mysql-connector-python tabulate
```

---

### 2️⃣ Setup MySQL

* Ensure MySQL is running
* Update credentials in code:

```python
host = 'localhost'
user = 'root'
password = 'your_password'
```

---

### 3️⃣ Run the Program

```bash
python main.py
```

---

## 🧩 Database Structure

The system automatically creates required tables if not present, including:

* `teacher`
* `kindergarden`, `class_1`, `class_2`, ... `class_5`
* `leave_request_teacher`
* `leave_request_student`
* `payroll`
* `classes`
* `grants`
* `feedback`
* `event`
* `cbse_news`
* `government_policies`
* `faq`
* `admission_forms`
* `bills`

---

## 🖥️ Application Flow

1. Program starts with main menu
2. User selects role (Head/Staff/Student)
3. Login authentication
4. Access role-specific functionalities
5. Perform operations via menu-driven interface

---

## 📚 Learning Outcomes

Through this project, I learned:

* Database integration using Python
* Writing SQL queries (CRUD operations)
* Menu-driven program design
* Handling multiple user roles
* Building real-world logic systems

---

## ⚠️ Limitations

* CLI-based (no graphical interface)
* Basic security (no encryption)
* Separate tables for each class (not scalable)
* No error handling for invalid inputs

---

## 🔮 Future Improvements

* Convert to GUI using Tkinter ✅ *(in progress)*
* Convert to full-stack web app (Node.js + MongoDB)
* Improve database normalization
* Add authentication security
* Implement modular code structure

---

## 📌 Author

**Tejwardeep Singh**
B.Tech CSE (2024–2028)

---

## ⭐ Note

This project marks the foundation of my development journey:

👉 Started as a **Class 12 CLI project**
👉 Now evolving into:

* GUI application (Tkinter)
* Web application (Pandori project)

---

## 📎 Reference

Full source code available here:


---

## 💬 Feedback

Suggestions and improvements are always welcome!

# 🎓 Student Portal – Software Engineering Project

This repository contains a complete **Student Portal Web Application** developed using **Flask** as part of the Software Engineering course.

The system is designed to simulate a real university portal where **students** and **instructors** can manage courses, grades, announcements, and profiles through a secure web interface.

The project follows clean architecture principles and is fully ready for evaluation, discussion, and local execution by instructors or teaching assistants.

---

## 🔄 CI/CD (GitHub Actions)

The project uses GitHub Actions to ensure code quality and stability.

![CI - Tests](https://github.com/ahkngc/Student_Portal/actions/workflows/ci-tests.yml/badge.svg)
![CI - Smoke](https://github.com/ahkngc/Student_Portal/actions/workflows/ci-smoke.yml/badge.svg)
![CI - Compile](https://github.com/ahkngc/Student_Portal/actions/workflows/ci-compile.yml/badge.svg)
![CI - Security](https://github.com/ahkngc/Student_Portal/actions/workflows/ci-security.yml/badge.svg)

All workflows can be viewed here:  
https://github.com/ahkngc/Student_Portal/actions

---

## 📋 Project Management

Project tasks, issues, and progress are managed using a GitHub Project Board.  
The project board is public and linked directly to the repository issues.

**Project Board:**  
https://github.com/users/ahkngc/projects/3

---

## 📌 Project Description

The Student Portal is a **role-based system** that supports two main user types:

- **Students**
- **Instructors**

Each role has different permissions and available features.  
The system is built using Flask with the **App Factory Pattern** and **Blueprint-based modular structure**.

---

## 🚀 Main Features

### Authentication & Authorization
- Login and logout system
- Session-based authentication
- Role-based access control (Student / Instructor)
- Protected routes using custom decorators

### Dashboard
- **Student Dashboard**
  - Number of enrolled courses
  - Recent grades
  - Latest announcements
- **Instructor Dashboard**
  - Total students
  - Total courses
  - Grades count
  - Announcements count

### Courses
- View all available courses
- Enroll and unenroll (Students)
- Create new courses (Instructors)

### Grades
- Students can view their grades
- Instructors can add grades for students

### Announcements
- Instructors can post announcements
- Students can view announcements feed

### Search
- Search courses by code or title
- Search announcements by title or content

### Profile
- View profile information
- Change password

---

## 🛠 Technology Stack

- **Language:** Python
- **Framework:** Flask
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Migrations:** Flask-Migrate
- **Frontend:** Jinja2 Templates + CSS
- **Testing:** Pytest
- **CI/CD:** GitHub Actions

---

## 🧱 Architecture Overview

- Flask **App Factory** (`create_app`)
- Feature-based **Blueprints**
- Services layer for business logic
- Models layer for database entities
- Clear separation of concerns for maintainability

---

## 📂 Project Structure (Overview)


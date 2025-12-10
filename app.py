from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "secret_key"
class Student:
    def __init__(self, student_id, email, password, name, age, class_, phone):
        self.id = student_id
        self.email = email
        self.password = password
        self.name = name
        self.age = age
        self.class_ = class_
        self.phone = phone
    
         # Issue 6
    def update_info(self, name, phone):
        self.name = name
        self.phone = phone
        
        
#issue 7
class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        students = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        sid, email, pwd, name, age, cls, phone = line.split(",")
                        students.append(Student(sid, email, pwd, name, age, cls, phone))
        return students        
        
         # Issue 8
    def save_students(self):
        with open(self.filename, "w") as f:
            for s in self.students:
                f.write(f"{s.id},{s.email},{s.password},{s.name},{s.age},{s.class_},{s.phone}\n")
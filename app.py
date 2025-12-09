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

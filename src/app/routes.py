from app import app, get_conn
from flask import render_template, redirect, url_for
from app.forms import StudentCreateForm

# TODO #1 list all students 
@app.route('/students')
def list_students():
    pass

# TODO #2 using a form, allow new students to be added
@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    pass

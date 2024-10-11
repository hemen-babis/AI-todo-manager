"""
Author: Hemen Babis
Date: February 2, 2023
Description: Flask-based AI-powered To-Do List Manager. The application allows users to add, edit, delete, 
and prioritize tasks using an AI model to predict task priority based on importance, due date, and description length.
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(10), nullable=False)
    importance = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"

import joblib

# Load the trained model
model = joblib.load('task_priority_model.pkl')

def calculate_priority(task):
    due_date = datetime.strptime(task.due_date, '%Y-%m-%d')
    days_left = (due_date - datetime.now()).days
    description_length = len(task.description)

    # Create feature array (importance, days_left, description_length)
    features = np.array([[task.importance, days_left, description_length]])
    
    # Predict priority using AI model
    priority_score = model.predict(features)[0]
    return priority_score

# Create the database
with app.app_context():
    db.create_all()

# Route to add or edit a task
@app.route('/add_task', methods=['POST'])
def add_task():
    task_id = request.form.get('task_id')  # Get task_id from the form
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    importance = int(request.form['importance'])

    # Check if task_id exists (i.e., we are editing an existing task)
    if task_id:
        task = Task.query.get(task_id)
        if task:
            task.title = title
            task.description = description
            task.due_date = due_date
            task.importance = importance
            db.session.commit()
            return jsonify(success=True)
    else:
        # Create a new task
        new_task = Task(title=title, description=description, due_date=due_date, importance=importance)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(success=True)

# Route to mark a task as complete or incomplete
@app.route('/complete_task', methods=['POST'])
def complete_task():
    task_id = int(request.form['task_id'])
    task = Task.query.get(task_id)
    task.completed = not task.completed  # Toggle the completed status
    db.session.commit()
    return jsonify(success=True)

# Route to delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_id = int(request.form['task_id'])
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)

# Route to display the task list (incomplete and complete)
@app.route('/')
def index():
    # Fetch incomplete tasks and order them by importance (descending)
    incomplete_tasks = Task.query.filter_by(completed=False).order_by(Task.importance.desc()).all()

    # Fetch completed tasks and order them by importance (descending)
    completed_tasks = Task.query.filter_by(completed=True).order_by(Task.importance.desc()).all()

    return render_template('index.html', incomplete_tasks=incomplete_tasks, completed_tasks=completed_tasks)

if __name__ == '__main__':
    app.run(debug=True)

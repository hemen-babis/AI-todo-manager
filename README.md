# AI-Powered To-Do List Manager

![To-Do List Manager](https://img.shields.io/badge/status-active-brightgreen.svg)

## Project Description
The **AI-Powered To-Do List Manager** is a Flask-based web application that helps users manage their tasks efficiently. The application leverages a machine learning model to predict the priority of tasks based on their **importance**, **due date**, and **description length**. Tasks are automatically sorted by their predicted priority, allowing users to focus on the most important and urgent tasks.

The system allows users to:
- Add, edit, complete, delete tasks
- View tasks in order of their AI-predicted priority
- Separate tasks into "Incomplete" and "Completed" categories
- Revert tasks back to incomplete from the completed section

## Features
- **AI-Powered Task Prioritization**: Uses an AI model (Decision Tree Regressor) to predict task priorities based on importance, due date, and task description.
- **Task Management**: Add, edit, complete, and delete tasks.
- **Dynamic Task Sorting**: Tasks are sorted automatically by their priority, helping users focus on what matters most.
- **Separate Incomplete/Completed Tasks**: View tasks based on their completion status with the option to revert completed tasks back to incomplete.
- **Modern UI Design**: Clean, responsive interface designed for a smooth user experience.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Machine Learning**: Scikit-learn (Decision Tree Regressor)
- **Database**: SQLite (via Flask SQLAlchemy)
- **AI Model**: A machine learning model to predict task priority based on task features.

## Installation and Setup
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/hemen-babis/AI-todo-manager.git
    cd AI-todo-manager
    ```

2. **Set up a virtual environment**:
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Train the AI model** (optional if `task_priority_model.pkl` is not already available):
    - Run the `train_model.py` script to generate the task priority model.
    ```bash
    python train_model.py
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage
1. **Adding a Task**:
   - Use the form at the top of the page to add a new task. Provide the task title, description, due date, and importance (1-5).
   
2. **Editing a Task**:
   - Click the "Edit" button next to any task to prefill the form. Modify the details and save the changes.

3. **Completing a Task**:
   - Click the "Complete" button to mark a task as complete. Completed tasks will be moved to the "Completed Tasks" section.

4. **Deleting a Task**:
   - Use the "Delete" button to remove a task permanently.

5. **Reverting a Task**:
   - In the "Completed Tasks" section, click "Undo Complete" to move a task back to the incomplete section.

![Screenshot 2024-10-10 210009](https://github.com/user-attachments/assets/f8e7b592-5675-4491-befe-e0196c9ef9bf)
![image](https://github.com/user-attachments/assets/828e1368-2ed5-4da4-8a31-24634997383f)


## AI Model Details
The AI model is trained using a **Decision Tree Regressor** from **Scikit-learn**. It predicts the priority of tasks based on:
- **Importance**: A user-given importance score (1-5).
- **Days Left Until Due**: How close the due date is.
- **Task Description Length**: The length of the task description, used as a rough proxy for task complexity.

## Contributing
Feel free to open an issue or submit a pull request if you have suggestions or want to contribute to this project.

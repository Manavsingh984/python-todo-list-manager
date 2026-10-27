# Personal To-Do List Manager 📝

A simple command-line To-Do List Manager built using Python.

This project allows users to organise their daily tasks by adding, viewing, completing, and deleting tasks. It also uses Python file handling to save tasks permanently.

## Features

- Add new tasks.
- View all existing tasks.
- Mark tasks as completed.
- Delete unwanted tasks.
- Save tasks automatically using file handling.
- Handle invalid task numbers using exception handling.
- Preserve tasks even after closing the program.

## Technologies Used

- Python 3
- File Handling
- Lists
- Functions
- Loops and Conditional Statements
- Exception Handling

## Project Structure

```text
Personal-ToDo-List-Manager/
│
├── main.py
├── todo_tasks.txt
├── README.md
└── .gitignore
```

Note: `todo_tasks.txt` is created automatically when a task is saved.

## How to Run

1. Install Python 3.
2. Clone this repository.
3. Open the project folder.
4. Run the following command:

```bash
python main.py
```

## Sample Output

```text
========== TO-DO LIST MANAGER ==========

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice: 1
Enter a new task: Complete Python project
Successfully added!
```

## What I Learned

While building this project, I practised:

- Working with Python lists.
- Reading and writing text files.
- Creating reusable functions.
- Handling invalid user inputs.
- Building menu-driven programs.
- Storing and managing data between program executions.

## Future Improvements

- Add task deadlines.
- Add task priorities.
- Introduce a graphical user interface (GUI).

---

Created as a Python practice project while strengthening my programming fundamentals and learning Git and GitHub.
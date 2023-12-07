import sqlite3
import datetime

# Create a SQLite database and a 'tasks' table
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date DATE,
        priority INTEGER,
        completed BOOLEAN DEFAULT 0
    )
''')
conn.commit()

def add_task(title, description, due_date, priority):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority)
        VALUES (?, ?, ?, ?)
    ''', (title, description, due_date, priority))
    conn.commit()
    print("Task added successfully!")

def update_task(task_id, title=None, description=None, due_date=None, priority=None, completed=None):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    update_query = 'UPDATE tasks SET '
    params = []
    if title:
        update_query += 'title=?, '
        params.append(title)
    if description:
        update_query += 'description=?, '
        params.append(description)
    if due_date:
        update_query += 'due_date=?, '
        params.append(due_date)
    if priority:
        update_query += 'priority=?, '
        params.append(priority)
    if completed is not None:
        update_query += 'completed=?, '
        params.append(completed)
    update_query = update_query.rstrip(', ')
    update_query += ' WHERE id=?'
    params.append(task_id)

    cursor.execute(update_query, tuple(params))
    conn.commit()
    print("Task updated successfully!")

def remove_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    print("Task removed successfully!")

def list_tasks(order_by='due_date'):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM tasks ORDER BY {order_by}')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# Example usage:
add_task("Complete Project", "Finish the project by the deadline", "2023-12-31", 2)
update_task(1, priority=1)
remove_task(2)
list_tasks('priority')

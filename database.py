import sqlite3
from datetime import date

DB_NAME = "data/lifeos.db"


# ==========================================
# CONNECTION
# ==========================================

def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================
# CREATE TABLES
# ==========================================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    # Habits
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_name TEXT NOT NULL,
        category TEXT,
        created_date TEXT DEFAULT CURRENT_DATE
    )
    """)

    # Habit Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habit_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER,
        completed INTEGER,
        log_date TEXT,
        FOREIGN KEY(habit_id) REFERENCES habits(id)
    )
    """)

    # Planner
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planner(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        task_time TEXT,
        priority TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    # Goals
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goal TEXT,
        status INTEGER
    )
    """)

    # Journal
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT,
        energy INTEGER,
        note TEXT,
        journal_date TEXT
    )
    """)

    conn.commit()
    conn.close()
    # ==========================================
# HABITS
# ==========================================

def add_habit(name, category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO habits(
            habit_name,
            category
        )
        VALUES (?, ?)
    """, (name, category))

    conn.commit()
    conn.close()


def get_habits():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            habit_name,
            category,
            created_date
        FROM habits
        ORDER BY id DESC
    """)

    habits = cursor.fetchall()

    conn.close()

    return habits


def delete_habit(habit_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM habits WHERE id=?",
        (habit_id,)
    )

    cursor.execute(
        "DELETE FROM habit_logs WHERE habit_id=?",
        (habit_id,)
    )

    conn.commit()
    conn.close()


# ==========================================
# HABIT LOGS
# ==========================================

def save_habit_log(habit_id, completed):

    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()

    cursor.execute("""
        SELECT id
        FROM habit_logs
        WHERE habit_id=? AND log_date=?
    """, (habit_id, today))

    existing = cursor.fetchone()

    if existing:

        cursor.execute("""
            UPDATE habit_logs
            SET completed=?
            WHERE id=?
        """, (completed, existing["id"]))

    else:

        cursor.execute("""
            INSERT INTO habit_logs(
                habit_id,
                completed,
                log_date
            )
            VALUES (?, ?, ?)
        """, (habit_id, completed, today))

    conn.commit()
    conn.close()


def get_habit_status(habit_id):

    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()

    cursor.execute("""
        SELECT completed
        FROM habit_logs
        WHERE habit_id=? AND log_date=?
    """, (habit_id, today))

    row = cursor.fetchone()

    conn.close()

    if row:
        return bool(row["completed"])

    return False


# ==========================================
# DASHBOARD
# ==========================================

def get_today_progress():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM habits
    """)

    total = cursor.fetchone()["total"]

    cursor.execute("""
        SELECT COUNT(*) AS completed
        FROM habit_logs
        WHERE completed=1
        AND log_date=date('now')
    """)

    completed = cursor.fetchone()["completed"]

    conn.close()

    if total == 0:
        return 0, 0, 0

    progress = int((completed / total) * 100)

    return completed, total, progress


def get_life_score():

    _, _, progress = get_today_progress()

    return progress
# ==========================================
# PLANNER
# ==========================================

def add_task(task, task_time, priority):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO planner(
            task,
            task_time,
            priority
        )
        VALUES (?, ?, ?)
    """, (task, task_time, priority))

    conn.commit()
    conn.close()


def get_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            task,
            task_time,
            priority,
            completed
        FROM planner
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def update_task(task_id, completed):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE planner
        SET completed=?
        WHERE id=?
    """, (completed, task_id))

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM planner
        WHERE id=?
    """, (task_id,))

    conn.commit()
    conn.close()




# ==========================================
# GOALS
# ==========================================

def add_goal(goal):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO goals(goal, status)
        VALUES (?, 0)
    """, (goal,))

    conn.commit()
    conn.close()


def get_goals():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM goals
        ORDER BY id DESC
    """)

    goals = cursor.fetchall()

    conn.close()

    return goals


def update_goal(goal_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE goals
        SET status=?
        WHERE id=?
    """, (status, goal_id))

    conn.commit()
    conn.close()


def delete_goal(goal_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM goals
        WHERE id=?
    """, (goal_id,))

    conn.commit()
    conn.close()


# ==========================================
# JOURNAL
# ==========================================

def add_journal(mood, energy, note):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO journal(
            mood,
            energy,
            note,
            journal_date
        )
        VALUES (?, ?, ?, ?)
    """, (
        mood,
        energy,
        note,
        date.today().isoformat()
    ))

    conn.commit()
    conn.close()


def get_journal():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM journal
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================================
# ANALYTICS
# ==========================================

def total_habits():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM habits")

    total = cursor.fetchone()["total"]

    conn.close()

    return total


def total_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM planner")

    total = cursor.fetchone()["total"]

    conn.close()

    return total


def completed_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM planner
        WHERE completed=1
    """)

    total = cursor.fetchone()["total"]

    conn.close()

    return total

# ==========================================
# ANALYTICS
# ==========================================

def total_goals():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM goals")

    total = cursor.fetchone()["total"]

    conn.close()

    return total


def total_journal():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM journal")

    total = cursor.fetchone()["total"]

    conn.close()

    return total
# ==========================================
# INITIALIZE DATABASE
# ==========================================

create_tables()
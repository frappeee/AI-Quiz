import sqlite3
import os

db_path = os.path.join(os.getcwd(), "quiz_database.db")
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_table (
  topic TEXT,
  question TEXT,
  option_a TEXT,
  option_b TEXT,
  option_c TEXT,
  option_d TEXT,
  correct_answer CHAR(1)
)
""")

connection.commit()
connection.close()
print("Database initialized.")
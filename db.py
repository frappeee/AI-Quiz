import sqlite3

def get_connection():
    return sqlite3.connect("quiz_database.db", check_same_thread=False)

def create_quiz(topic, quiz_data):
    conn = get_connection()
    cursor = conn.cursor()
    for q in quiz_data:
        cursor.execute("""
            INSERT INTO quiz_table (topic, question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            topic,
            q['q'],
            q['A'],
            q['B'],
            q['C'],
            q['D'],
            q['correct']
        ))
    conn.commit()
    conn.close()

def get_quiz(topic):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT question, option_a, option_b, option_c, option_d, correct_answer
        FROM quiz_table WHERE topic = ?
    """, (topic,))
    rows = cursor.fetchall()
    conn.close()
    
    # Debug print to check retrieved data
    print("Retrieved quiz data:", rows)
    
    return [
        {
            'question': row[0],
            'A': row[1],
            'B': row[2],
            'C': row[3],
            'D': row[4],
            'correct_answer': row[5]
        }
        for row in rows
    ]

def get_topics():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT topic FROM quiz_table")
    topics = [row[0] for row in cursor.fetchall()]
    conn.close()
    return topics

def delete_quiz(topic):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quiz_table WHERE topic = ?", (topic,))
    conn.commit()
    conn.close()
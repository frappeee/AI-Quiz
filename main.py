import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_quiz(topic, number_of_questions=5):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "AI Quiz App"
    }

    prompt = (
        f"Generate {number_of_questions} multiple-choice quiz questions about '{topic}'. "
        "Each question must have:\n"
        "- 'q': The question text\n"
        "- 'A': Option A\n"
        "- 'B': Option B\n"
        "- 'C': Option C\n"
        "- 'D': Option D\n"
        "- 'correct': The correct answer (A, B, C, or D)\n"
        "Return ONLY a valid JSON array of these objects, nothing else.\n"
        "Example:\n"
        "[{\"q\": \"What is 2+2?\", \"A\": \"3\", \"B\": \"4\", \"C\": \"5\", \"D\": \"6\", \"correct\": \"B\"}]"
    )

    body = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=body)
    result = response.json()

    try:
        answer = result["choices"][0]["message"]["content"]
        print("Raw AI response:", answer)  # Debug print
        quiz_data = json.loads(answer)
        print("Parsed quiz data:", quiz_data)  # Debug print
        return quiz_data
    except Exception as e:
        print("Error parsing response:", e)
        print("Full response:", result)
        return []
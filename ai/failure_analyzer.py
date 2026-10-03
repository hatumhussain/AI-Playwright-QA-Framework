import requests

def analyze_failure(test_name, error_message):
    prompt = f"""
You are a senior QA automation engineer.

Analyze this Playwright UI test failure.

Test name: {test_name}
Error: {error_message}

Provide:
1. Possible root cause
2. Why it may have happened
3. Debugging steps
4. Suggested fix

Keep the response concise and beginner-friendly.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"]
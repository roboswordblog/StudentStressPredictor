import json
from openai import OpenAI

client = OpenAI()

def returnWorkflow(data):
    prompt = """
You are an assistant that analyzes a student's homework tasks.

The user will provide a list of activities. Based on this, you must:

1. Create an efficient and realistic workflow order for completing the tasks.
2. Estimate the student's stress level.
3. Determine if the workload is too much for one night.

Return ONLY a valid JSON object with this exact structure:

{
  "workflow": "A clear step-by-step plan written in plain text",
  "stress": "low | medium | high",
  "overdoing": true or false
}

User tasks:
""" + data

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    # Safe way to get the text
    text = ""
    if hasattr(response, "output") and response.output:
        for item in response.output:
            if hasattr(item, "content") and item.content:
                for c in item.content:
                    if hasattr(c, "text") and c.text:
                        text += c.text

    if not text:
        raise ValueError("No response text from the API")

    # Convert to Python dict
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Failed to parse JSON. Raw response: {text}")

    return result
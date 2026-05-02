from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant who explains things simply in very few lines."}
]


def ask_ai(prompt):
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    # limit memory
    if len(messages) > 20:
        messages.pop(1)

    return reply


def decide_action(user_input):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
Reply with ONE word:

math → if it involves numbers or calculation  
chat → everything else
"""
            },
            {"role": "user", "content": user_input}
        ]
    )

    action = response.choices[0].message.content.strip().lower()

    if "math" in action:
        return "math"
    else:
        return "chat"

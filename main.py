from ai import ask_ai, decide_action
from tools import calculator

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    if not user_input.strip():
        continue

    action = decide_action(user_input)

    if action == "math":
        result = calculator(user_input)

        if result:
            print("TOOL:", result)
        else:
            print("TOOL: Could not calculate. Switching to AI...")
            print("AI:", ask_ai(user_input))
    else:
        print("AI:", ask_ai(user_input))

    print("-" * 100)

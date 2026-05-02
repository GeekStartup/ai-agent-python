def calculator(text):
    text = text.lower()

    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("times", "*")
    text = text.replace("multiply", "*")
    text = text.replace("divide", "/")
    text = text.replace("calculate", "")

    try:
        return str(eval(text))
    except:
        return None

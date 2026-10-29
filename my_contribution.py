def welcome_message(name: str) -> str:
    return f"Hello, {name}! This message is from the main branch."


if __name__ == "__main__":
    print(welcome_message("Student"))
def welcome_message(name: str) -> str:
    return f"Welcome, {name}! This message is from the feature branch."


if __name__ == "__main__":
    print(welcome_message("Student"))
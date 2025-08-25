from input_functions import *


def main():
    username = get_username()
    current_questions = {}
    new_question(current_questions)
    print("Final Questions List:")
    for question in current_questions:
        print(f"- {question}")

if __name__ == "__main__":
    main()

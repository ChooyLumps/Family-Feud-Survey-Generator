from input_functions import *


def main():
    print("===================================")
    print("Welcome to Family Feud Survey Genorator!")
    print("===================================")
    name = get_username()
    current_questions = {}
    sequence = initial_navigator(current_questions, name)
    print("Thank you for using the Family Feud Servey Genorator. Goodbye!")


if __name__ == "__main__":
    main()

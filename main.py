from input_functions import *
from processing_functions import *


def main():
    print("===================================")
    print("Welcome to Family Feud Survey Genorator!")
    print("===================================")
    name = get_username()
    current_questions = {}
    sequence = initial_navigator(current_questions, name)
    print("Thank you for using the Family Feud Survey Genorator. Goodbye!")


if __name__ == "__main__":
    main()

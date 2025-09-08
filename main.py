from input_functions import *
from processing_functions import *


def main():
    print("===================================")
    print("Welcome to Family Feud Survey Genorator!")
    print("===================================")
    password = get_password() # Get the admin password
    current_questions = {}
    navigator(current_questions, password)
    print("Thank you for using the Family Feud Survey Genorator. Goodbye!")


if __name__ == "__main__":
    main()

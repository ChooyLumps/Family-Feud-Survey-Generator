from processing_functions import *

def get_password(): # Function to get the admin password
    return input("Please set the admin password: ")


def get_username(): # Function to get the user's name
    username = input("Please enter the name on your badge: ")
    print(f"Hello, {username}!")
    return username


def new_question(current_questions={}): # Function to impliment a new question
    question = input("Enter the new question: ") # Prompt user for a new question
    if question in current_questions: # Check if the question already exists
        print("This question already exists.")
    else: # If the question does not exist, add it to the dictionary
        current_questions[question] = {}
        print(f"Question '{question}' added.")
    if input("Would you like to add another question? (y/n): ").lower() == 'y': # Ask if the user wants to add another question
        new_question(current_questions)
    else: # If the user does not want to add another question, print the final questions list
        print("Finished adding questions.")
        print("Final Questions List:")
        for question in current_questions:
            print(f"- {question}")


def answer_questions(current_questions, name=''): # Function to answer questions
    if name == '': # If no name is provided, get the username
        name = get_username()
    if check_validity(current_questions, name): # Check if the survey can be taken
        print("===================================")
        print("Welcome to the survey!")
        print("Please answer the following questions as honestly as possible.")
        print("Your answers will be annonymous.")
        print("Spelling is important! Feel free to use Google to check your spelling.")
        consent = input("Got it? (y/n):\n").lower()
        if consent != 'y':
            print("===================================")
            print("Please read the instructions carefully before proceeding.")
            answer_questions(current_questions, name)
        print("Let's begin!")
        print("===================================")
        if check_username(name): # Check if the username is valid
            for question in current_questions: # Loop through each question
                print(f"{question}:")
                answer = input("Your answer: ").lower()
                add_answer(current_questions[question], answer)
            print("Thank you for answering the questions!")
            print("Have a great day!")
    return


def remove_question(current_questions): # Function to remove a question
    if not current_questions: # Check if there are no questions
        print("No questions available to remove.")
        return
    else: # If there are questions, prompt the user to remove one
        view_questions(current_questions)
        dead_index = int(input("Enter the number of the question you want to remove: ")) - 1
        if 0 =< dead_index < len(current_questions):
            dead_question = list(current_questions.keys())[dead_index]
            del current_questions[dead_question]
            print(f"Question '{dead_question}' removed.")
        else:
            print("Invalid question number.")
            remove_question(current_questions)
    if input("Would you like to remove another question? (y/n): ").lower() == 'y': # Ask if the user wants to remove another question
        remove_question(current_questions)
    else: # If the user does not want to remove another question, print the final questions
        return

def navigator(current_questions, password): # Function to determine the action type
    print("====================================")
    action = input("What would you like to do?\n-answer questions\n-view questions\n-add question\n-remove question\n-analyse answer\n-close program:\n").lower().split(" ")[0]
    if action == "add":
        new_question(current_questions)
    elif action == "remove":
        remove_question(current_questions)
    elif action == "answer":
        answer_questions(current_questions)
        lockout(password)
    elif action == "view":
        view_questions(current_questions)
    elif action == "analyse":
        analyse_answers(current_questions)
    elif action == "close":
        if input("Warning: If you close the program all questions will be deleted! Are you sure you want to close the program? (y/n):\n").lower() == 'y':
            return   
    else:
        print("Invalid action. Action may not be implimented yet")
    navigator(current_questions, name)


def lockout(password):
    attempt = input("Enter the password to continue: ") # Prompt user for the password
    if attempt == password: # Check if the password is correct
        return
    else: # If the password is incorrect, prompt the user to try again
        print("Incorrect password. Try again.")
        lockout(password)
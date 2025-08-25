from processing_functions import *

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

def answer_questions(current_questions, name): # Function to answer questions
    if not current_questions: # Check if there are no questions
        print("No questions available to answer.")
    else: # If there are questions, prompt the user to answer them
        print("====================================")
        name_check = input(f"Your name will not be linked to your answers.\nPlease confirm that the name on your badge is {name} (y/n):\n")
        if name_check == "y": # Check if the user confirmed their name
            age_check = input("Please enter your age:\n")
            if int(age_check) >= 18: # Check if the user is 18 or older
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
                for question in current_questions: # Loop through each question
                    print(f"{question}:")
                    answer = input("Your answer: ").lower()
                    add_answer(current_questions[question], answer)
                print("Thank you for answering the questions!")
                print("Have a great day!")
                return name
            else:
                print("Sorry, this survey is intended for adults only.")
        else:
            name = get_username()
            answer_questions(current_questions, name)

def initial_navigator(current_questions, name): # Function to determine the action type
    print("====================================")
    action = input("What would you like to do?\n-answer questions\n-view questions\n-add question\n-name change\n-analyse answer\n-close program:\n").lower().split(" ")[0]
    if action == "add":
        new_question (current_questions)
    elif action == "answer":
        name = answer_questions(current_questions, name)
        lockout(current_questions, name)
    elif action == "name":
        name = get_username()
    elif action == "view":
        view_questions(current_questions)
    elif action == "analyse":
        analyse_answers(current_questions)
    elif action == "close":
        if input("Warning: If you close the program all questions will be deleted! Are you sure you want to close the program? (y/n):\n").lower() == 'y':
            return   
    else:
        print("Invalid action. Action may not be implimented yet")
    initial_navigator(current_questions, name)


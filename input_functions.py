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

def view_questions(current_questions): # Function to view current questions
    if not current_questions: # Check if there are no questions
        print("No questions available.")
    else: # If there are questions, print them
        print("Current Questions:")
        for question in current_questions:
            print(f"- {question}")


def initial_navigator(current_questions): # Function to determine the action type
    print("====================================")
    action = input("What would you like to do?\n-answer questions\n-view questions\n-add question\n-name change\n-analyse answer\n-close program:\n").lower().split(" ")[0]
    if action == "add":
        new_question (current_questions)
    elif action == "name":
        get_username()
    elif action == "view":
        view_questions(current_questions)
    elif action == "close":
        if input("Warning: If you close the program all questions will be deleted! Are you sure you want to close the program? (y/n): ").lower() == 'y':
            return "close"    
    else:
        print("Invalid action. Action may not be implimented yet. Please choose 'add questions' or 'name change'.")
    initial_navigator(current_questions)


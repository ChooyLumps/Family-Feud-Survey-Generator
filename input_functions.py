def get_username(): # Function to get the user's name
    username = input("Please enter the name on your badge: ")
    print(f"Hello, {username}!")
    return username

def new_question(current_questions={}): # Function to impliment a new question
    question = input("Enter the new question: ") # Prompt user for a new question
    if question in current_questions: # Check if the question already exists
        print("This question already exists.")
    else: # If the question does not exist, add it to the dictionary
        current_questions[question] = []
        print(f"Question '{question}' added.")
    if input("Would you like to add another question? (y/n): ").lower() == 'y': # Ask if the user wants to add another question
        new_question(current_questions)
    else:
        print("Finished adding questions.")
        print("Final Questions List:")
        for question in current_questions:
            print(f"- {question}")

def initial_navigator(current_questions): # Function to determine the action type
    action = input("What would you like to do?\n-answer questions\n-view questions\n-add question\n-name change\n-analyse answer\n-close program: ").lower().split(" ")[0]
    if action == "add":
        new_question (current_questions)
    elif action == "name":
        get_username()
    elif action == "close":
        return "close"
    else:
        print("Invalid action. Action may not be implimented yet. Please choose 'add questions' or 'name change'.")
    initial_navigator(current_questions)


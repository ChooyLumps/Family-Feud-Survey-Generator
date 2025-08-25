def get_username(): # Function to get the user's name
    username = input("Please enter the name on your badge: ")
    print(f"Hello, {username}!")
    return username

def new_question(current_questions={}): # Function to impliment a new question
    question = input("Enter the new question: ")
    if question in current_questions:
        print("This question already exists.")
    else:
        current_questions[question] = []
        print(f"Question '{question}' added.")
    if input("Would you like to add another question? (y/n): ").lower() == 'y':
        new_question(current_questions)


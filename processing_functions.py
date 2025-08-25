
def view_questions(current_questions): # Function to view current questions
    if not current_questions: # Check if there are no questions
        print("No questions available.")
    else: # If there are questions, print them
        print("Current Questions:")
        for question in current_questions:
            print(f"- {question}")

def add_answer(question, answer): # Function to add an answer to a question
    if answer in question: # Check if the answer already exists
        question[answer] += 1
    else: # If the answer does not exist, add it to the dictionary
        question[answer] = 1

def lockout(current_questions, name):
    password = "ketchup_master_3000" # Set the password
    attempt = input("Enter the password to continue: ") # Prompt user for the password
    if attempt == password: # Check if the password is correct
        return
    else: # If the password is incorrect, prompt the user to try again
        print("Incorrect password. Try again.")
        lockout(current_questions, name)

def analyse_answers(current_questions): # Function to analyse answers
    if not current_questions: # Check if there are no questions
        print("No questions available to analyse.")
    else: # If there are questions, begin analysis
        for question in current_questions:
            print("====================================")
            print(f"Analysis for question: {question}")
            sorted_answers = sorted(current_questions[question], key=lambda x: current_questions[question][x], reverse=True)
            for answer in sorted_answers:
                print(f"- {answer}: {current_questions[question][answer]}")
            print("====================================")
            

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

def top_answers(question, total_answers): # Function to get the top answers for a question
    if not question: # Check if there are no answers
        print("No answers available for this question.")
        return
    sorted_answers = sorted(question, key=lambda x: question[x], reverse=True)
    print(f"Top answers for question '{question}':")
    for answer in sorted_answers:
        total_answers -= question[answer]
        if total_answers >= 0:
            print(f"- {answer}: {question[answer]}")
        else:
            ending_answer = question[answer] + total_answers
            print(f"- {answer}: {ending_answer}")
            break
    
def analyse_answers(current_questions): # Function to analyse answers
    if not current_questions: # Check if there are no questions
        print("No questions available to analyse.")
    else: # If there are questions, begin analysis
        if input("Would you like to analyse all answers or just the top answers? (all/top): ").lower() == 'all':
            total_answers = float('inf')
            for question in current_questions:
                print("====================================")
                print(f"Question: {question}")
                top_answers(current_questions[question], total_answers)
                print("====================================")
        else:
            total_answers = 50 # Set the total number of top answers to display
            for question in current_questions:
                print("====================================")
                print(f"Question: {question}")
                top_answers(current_questions[question], total_answers)
                print("====================================")
                
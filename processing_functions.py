
username_list = [] # List to store usernames for checking duplicates

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

def check_username(username): # Function to check if the username already exists
    if username in username_list: # Check if the username is already in the list
        print("It appears that you have already taken the survey.")
        return False
    else: # If the username is not in the list, add it to the list
        username_list.append(username)
        return True

def check_validity(current_questions, name):
    if not current_questions: # Check if there are no questions
        print("No questions available to answer.")
        return False
    else: # If there are questions, prompt the user to answer them
        print("====================================")
        name_check = input(f"Your name will not be linked to your answers.\nPlease confirm that the name on your badge is {name} (y/n):\n")
        if name_check == "y": # Check if the user confirmed their name
            if check_username(current_questions, name):
                age_check = input("Please enter your age:\n")
                if int(age_check) >= 18: # Check if the user is 18 or older
                    return True
                else:
                    print("Sorry, this survey is intended for adults only.")
                    return False
        else:
            print("Please ask admin to change your name.")
            return False
    
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
                